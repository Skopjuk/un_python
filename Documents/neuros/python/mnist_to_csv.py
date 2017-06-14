from mnist import MNIST
import os
mndata = MNIST('./python-mnist/data')
mndata.load_training()
mndata.load_testing()

def convert(imgf, labelf, outf, n):
    f = open(os.path.join('./python-mnist/data',imgf), "rb")
    o = open(os.path.join('./python-mnist/data',outf), "w")
    l = open(os.path.join('./python-mnist/data',labelf), "rb")

    f.read(16)
    l.read(8)
    images = []

    for i in range(n):
        image = [ord(l.read(1))]
        for j in range(28*28):
            image.append(ord(f.read(1)))
        images.append(image)

    for image in images:
        o.write(",".join(str(pix) for pix in image)+"\n")
    f.close()
    o.close()
    l.close()

convert("train-images-idx3-ubyte", "train-labels-idx1-ubyte",
        "mnist_train.csv", 60000)
convert("t10k-images-idx3-ubyte", "t10k-labels-idx1-ubyte",
        "mnist_test.csv", 10000)
