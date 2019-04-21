import tensorflow as tf

x_data = [[1,2,1,1],[2,1,3,2],[3,1,3,4],[4,1,5,5],[1,7,5,5],[1,2,5,6],[1,6,6,6],[1,7,7,7]]
y_data = [[0,0,1],[0,0,1],[0,0,1],[0,1,0],[0,1,0],[0,1,0],[1,0,0],[1,0,0,]]

X = tf.placeholder(tf.float32, shape=[None,len(x_data[0])])
Y = tf.placeholder(tf.float32, shape=[None,len(y_data[0])])
nb_classes = 3

W = tf.Variable(tf.random_normal([len(x_data[0]),nb_classes]), name='weight')
b = tf.Variable(tf.random_normal([nb_classes]),name='bias')

hypothesis = tf.nn.softmax(tf.matmul(X,W)+b)

cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(hypothesis), axis=1))
optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.1).minimize(cost)

predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted,Y),dtype=tf.float32))

with tf.Session() as sess:
	sess.run(tf.global_variables_initializer())

	for step in range(10001):
		cost_val, _ = sess.run([cost,optimizer],feed_dict={X: x_data, Y: y_data})
	#	sess.run(optimizer,feed_dict={X: x_data, Y: y_data})
		if step % 1000 ==0:
	#		print(step,sess.run(cost,feed_dict={X: x_data, Y: y_data}))
			print(step,cost_val)
	h,c,a = sess.run([hypothesis,predicted,accuracy],
			feed_dict={X:x_data,Y:y_data})
	print("\nHypothesis: ",h,"\nCorrect(Y): ",c,"\nAccuracy: ",a)
