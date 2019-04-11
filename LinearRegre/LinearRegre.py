import numpy as np
from metrics import r2_score

class LinearRegression:
    def __init__(self):
        self.coef_ = None  # 系数
        self.intercept_ = None  # 截距
        self._theta = None

    def fit_normal(self, X_train, y_train):
        '''根据训练数据集X_train, y_train训练,直接用偏导求极值公式计算theta'''
        assert X_train.shape[0] == y_train.shape[0], 'the size of X_train and y_train must be the same'
        X_b = np.hstack([np.ones([len(X_train), 1]), X_train])  # hstack 横向添加一列
        self._theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y_train)  # inv 取逆矩阵
        self.intercept_ = self._theta[0]
        self.coef_ = self._theta[1:]

        return self

    def fit_gd(self, X_train, y_train, eta=0.01, n_iters=1e4):
        '''根据训练数据X_train,y_train,使用批量梯度下降法训练'''
        assert X_train.shape[0] == y_train.shape[0], 'the size of X_train must be equal to the size of y_train'

        def J(theta, X_b, y):
            try:
                return np.sum((y - X_b.dot(theta)) ** 2) / len(y)
            except:
                return float('inf')

        def dJ(theta, X_b, y):
            return X_b.T.dot(X_b.dot(theta) - y) * 2. / len(y)

        def gradient_descent(X_b, y, initial_theta, eta, n_iters=1e4, epsilon=1e-8):
            theta = initial_theta
            cur_iter = 0

            while cur_iter < n_iters:
                gradient = dJ(theta, X_b, y)
                last_theta = theta
                theta = theta - eta * gradient
                if (abs(J(theta, X_b, y) - J(last_theta, X_b, y)) < epsilon):
                    break
                cur_iter += 1
            return theta

        X_b = np.hstack([np.ones((len(X_train), 1)), X_train])
        initial_theta = np.zeros(X_b.shape[1])
        self._theta = gradient_descent(X_b, y_train, initial_theta, eta, n_iters)
        self.intercept_ = self._theta[0]
        self.coef_ = self._theta[1:]
        return self

    def fit_sgd(self, X_train, y_train, n_iters=5, t0=5, t1=50):
        # 随机梯度下降法
        assert X_train.shape[0] == y_train.shape[0], \
            'the size of X_train must be equal to the size of y_train'
        assert n_iters >= 1

        def dJ_sgd(theta, X_b_i, y_i):
            return X_b_i * (X_b_i.dot(theta) - y_i) * 2.
            # return X_b_i.T.dot(X_b_i.dot(theta)-y_i)*2

        def sgd(X_b, y, initial_theta, n_iters, t0=5, t1=50):
            def learning_rate(t):
                return t0 / (t + t1)

            theta = initial_theta
            m = len(X_b)
            # 对所有的样本看n_iters遍
            for cur_iter in range(n_iters):
                indexes = np.random.permutation(m)
                X_b_new = X_b[indexes]
                y_new = y[indexes]
                for i in range(m):
                    gradient = dJ_sgd(theta, X_b_new[i], y_new[i])
                    theta = theta - learning_rate(cur_iter * m + i) * gradient

            return theta

        X_b = np.hstack([np.ones((len(X_train), 1)), X_train])
        initial_theta = np.random.randn(X_b.shape[1])
        self._theta = sgd(X_b, y_train, initial_theta, n_iters, t0, t1)
        self.intercept_ = self._theta[0]
        self.coef_ = self._theta[1:]

        return self

    def fit_msgd(self, X_train, y_train, n_iters=1e4, t0=5, t1=50, batch_size=10):
        # 小批量随机梯度下降
        assert X_train.shape[0] == y_train.shape[0], \
            'the size of X_train must be equal to the size of y_train'
        assert n_iters >= 1

        def J(theta, X_b, y):
            try:
                return np.sum((y - X_b.dot(theta)) ** 2) / len(y)
            except:
                return float('inf')

        def dJ(theta, X_b, y):
            return X_b.T.dot(X_b.dot(theta) - y) * 2. / len(y)

        def msgd(X_b, y, initial_theta, t0, t1, batch_size, n_iters, epsilon=1e-8):

            def learning_rate(t):
                return t0 / (t + t1)

            theta = initial_theta
            cur_iter = 0

            while cur_iter < n_iters:
                indexes = np.random.randint(0, len(X_b), batch_size)
                X_b_new = X_b[indexes]
                y_b_new = y[indexes]
                gradient = dJ(theta, X_b_new, y_b_new)
                last_theta = theta
                theta = theta - learning_rate(cur_iter) * gradient
                if (abs(J(theta, X_b, y) - J(last_theta, X_b, y)) < epsilon):
                    break
                cur_iter += 1

            return theta

        X_b = np.hstack([np.ones((len(X_train), 1)), X_train])
        initial_theta = np.random.randn(X_b.shape[1])
        self._theta = msgd(X_b, y_train, initial_theta, t0, t1, batch_size, n_iters)
        self.intercept_ = self._theta[0]
        self.coef_ = self._theta[1:]

        return self

    def predict(self, X_predict):
        assert self.intercept_ is not None and self.coef_ is not None, 'must fit before predict'
        assert X_predict.shape[1] == len(self.coef_), 'the feature number of X_predict must be equal to X_train'
        X_b = np.hstack([np.ones((len(X_predict), 1)), X_predict])
        return X_b.dot(self._theta)

    def score(self, X_test, y_test):
        y_predict = self.predict(X_test)
        return r2_score(y_test, y_predict)
