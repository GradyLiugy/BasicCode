'''
在Python的sklearn工具包中有SVM算法， 首先引入工具包

from sklearn import svm


SVM 既可以做分类，也可以做回归。
当用 SVM 做回归的时候，我们可以使用 SVR 或 LinearSVR。SVR 的英文是 Support Vector Regression
当用 SVM 做分类的时候，我们使用的是 SVC 或 LinearSVC。SVC 的英文是 Support Vector Classification。

如何创建一个SVM分类器呢？
首先使用SVC的构造函数：

model = svm.SVC(kernel=‘rbf’, C=1.0, gamma=‘auto’) #这里有三个重要的参数 kernel、C 和 gamma。

kernel代表核函数的选择，有四种选择，默认rbf，即高斯核函数
    1.linear：线性核函数,是在数据线性可分的情况下使用的，运算速度快，效果好。不足在于它不能处理线性不可分的数据。
    2.poly：多项式核函数,多项式核函数可以将数据从低维空间映射到高维空间，但参数比较多，计算量大。
    3.rbf：高斯核函数（默认）,高斯核函数同样可以将样本映射到高维空间，
        但相比于多项式核函数来说所需的参数比较少，通常性能不错，所以是默认使用的核函数。
    4.sigmoid：sigmoid 核函数,sigmoid 经常用在神经网络的映射中。
        因此当选用 sigmoid 核函数时，SVM 实现的是多层神经网络。

参数 C 代表目标函数的惩罚系数，惩罚系数指的是分错样本时的惩罚程度，默认情况下为 1.0。
    当 C 越大的时候，分类器的准确性越高，但同样容错率会越低，泛化能力会变差。
    相反，C 越小，泛化能力越强，但是准确性会降低。

参数 gamma 代表核函数的系数，默认为样本特征数的倒数，即 gamma = 1 / n_features。

在创建 SVM 分类器之后，就可以输入训练集对它进行训练。

我们使用 model.fit(train_X,train_y)，传入训练集中的特征值矩阵 train_X 和分类标识 train_y。
特征值矩阵就是我们在特征选择后抽取的特征值矩阵（当然你也可以用全部数据作为特征值矩阵）；
分类标识就是人工事先针对每个样本标识的分类结果。这样模型会自动进行分类器的训练。
我们可以使用 prediction=model.predict(test_X) 来对结果进行预测，
传入测试集中的样本特征矩阵 test_X，可以得到测试集的预测分类结果 prediction。

同样我们也可以创建线性 SVM 分类器

使用 model=svm.LinearSVC()。在 LinearSVC 中没有 kernel 这个参数，限制我们只能使用线性核函数。
由于 LinearSVC 对线性分类做了优化，对于数据量大的线性可分问题，使用 LinearSVC 的效率要高于 SVC。

如果你不知道数据集是否为线性，可以直接使用 SVC 类创建 SVM 分类器。
在训练和预测中，LinearSVC 和 SVC 一样，都是使用 model.fit(train_X,train_y) 和 model.predict(test_X)。


支持向量机实战：见breast_linearsvm.py 和 breast_svm.py
'''

