# testing each model individually
# read the files for generating data
exec(open("./get_data.py").read())

# pick a model:    5:OverFeat, 8:our made-up model, 9:AlexNet, 11:Inception.v4.
model_to_fit = 9
y_conv = y_mod[model_to_fit-1]
MeanSquareCost, y_conv_flipped = cost_tensor(y_conv)

variables_to_restore = slim.get_variables(scope="ENSAI/EN_Model" + str(model_to_fit))
# restore_file = path of file with network weights
restore_file = "data/trained_weights/model_" + str(model_to_fit) + ".ckpt"
restorer = tf.train.Saver(variables_to_restore)

# The image is shifted in a central area with a side of max_xy_range (arcsec)
# during training or testing.
max_xy_range = 0.5
# If True, the noise rms will be chosen randomly for each sample with a max of
# max_noise_rms.
variable_noise_rms = True
# maximum rms of noise data
max_noise_rms = 0.1
# num_samp = number of test samples
num_samp = 1000
# chunk_size = batch number: how many test examples to pass at one time.
chunk_size = 50


# X = numpy array holding the images
X = np.zeros((num_samp, numpix_side * numpix_side), dtype='float32')
# Y = numpy array holding the lens parameters
# Here, Y is only used to flip for the x-y ellipticity
Y = np.zeros((num_samp, num_out), dtype='float32')
# Predictions = predicted lens parameters
Predictions = np.zeros((num_samp, num_out), dtype='float32')
mag = np.zeros((num_samp, 1))
read_data_batch(X, Y, mag, max_num_test_samples, 'test')


sess = tf.Session()        # launches tensorflow session
sess.run(tf.global_variables_initializer())
restorer.restore(sess, restore_file)        # restores saved weights


cost = 0.0
ind_t = range(num_samp)
sum_rms = 0
num_chunks = num_samp/chunk_size

# loop over our samples
# We can't give all of the test data at once because of limited gpu memory)
for it in range(int(num_chunks)):
    print(it)
    xA = X[ind_t[0 + chunk_size * it: chunk_size + chunk_size * it]]
    yA = Y[ind_t[0 + chunk_size * it: chunk_size + chunk_size * it]]
    # evaluate cost
    cost  = cost + sess.run(MeanSquareCost, feed_dict={x: xA, y_: yA})
    # A = network prediction for parameters
    A = sess.run(y_conv, feed_dict={x: xA})
    # B = the same prediction with the ellipticity flipped
    B = sess.run(y_conv_flipped, feed_dict={x: xA})
    # Correct "Prediction" for the flip.
    Predictions[ind_t[0 + chunk_size * it: chunk_size + chunk_size * it], :] \
            = get_rotation_corrected(A, B,
            Y[ind_t[0 + chunk_size * it: chunk_size + chunk_size * it], :])
    sum_rms = sum_rms + np.std(Predictions[ind_t[0 + chunk_size*it: chunk_size
            + chunk_size*it], :] -Y[ind_t[0 + chunk_size * it: chunk_size
            + chunk_size * it], :], axis = 0)
    print(np.array_str(sum_rms/it, precision=2))
