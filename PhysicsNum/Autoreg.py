import numpy as np
import matplotlib.pyplot as plt
from Linearreg import Linearreg, ForceLinearreg
from scipy.optimize import curve_fit

def GaussianFit(xval, yval):
    mean = sum(xval * yval)/sum(yval)
    guesssigma = np.sqrt(sum(yval * (xval - mean)**2) / sum(yval))
    func = lambda x, a, mu, sigma: a*np.exp(-(x - mu)**2/(2*sigma**2))
    try:
        Fit, covarience = curve_fit(func, xval, yval, p0 = [max(yval), mean, guesssigma])
    except:
        raise TypeError("Cant compute")
    Gaussian = lambda x: Fit[0]*np.exp(-(x-Fit[1])**2/(2*Fit[2]**2))
    return GaussianFit, (Fit[0], Fit[1], Fit[2])

def Exponentialdecay(xval, yval):
    try:
        xval = np.array(xval); yval = np.array(yval)
    except:
        pass
    for i in range(1,len(yval)):
        if yval[i]>yval[i-1]:
            yval[i] = yval[i-1]
    Exponential = lambda x, A, tau, b: A*np.exp(-x/tau) + b
    try:
        Fit, Covarience = curve_fit(Exponential, xval, yval, p0 = [max(ylist), 10, 100])
        func = lambda x: Fit[0] * np.exp(-x/Fit[1]) + Fit[2]
        return func
    except:
        for i in range(1,len(yval)):
            if yval[i]>yval[i-1]:
                yval[i] = yval[i-1]
        Fit, Covarience = curve_fit(Exponential, xval, yval, p0 = [max(ylist), 10, 100])
        func = lambda x: Fit[0] * np.exp(-x/Fit[1]) + Fit[2]
        return func, (Fit[0], Fit[1], Fit[2])


class Autoreg():
    """A class that takes the parameters of which how to fit the data. Tries to automate the process."""
    Regressions = {
        "Linear" : Linearreg,
        "Linear0" : ForceLinearreg,
        "Gaussian" : GaussianFit
    }
    Background = {
        "Exponentialdecay" : Exponentialdecay
    }
    def __init__(self, xval, yval, Fit = "Linear", Background = "Exponentialdecay"):
        """ """
        if not isinstance((xval, yval), (np.generic, np.ndarray)):
            xval = np.array(xval); yval = np.array(yval)
        self.xval = xval; self.yval = yval
        self.Fit = Fit
        try:
            self.Reg = self.Regressions[Fit]
        except:
            raise TypeError("[Autoreg]: The regressionmethod is not implemented.")
        self.Compute()

    def Compute(self):
        if self.Fit == "Gaussian":
            z = 2
            FitsMade = []
            print(len(self.xval))
            for i in range(100, len(self.xval)-2,z):
                if i >= 1750: break
                for j in range(i+10, i + 150, z): #Arbitrary values. Using these to just set a scale of which the gaussian computes
                    if j + 75 >len(self.xval):#No more data to fit.
                        break
                    print(i,j)
                    try:
                        func = self.Reg(self.xval[i:j], self.yval[i:j])
                        if func[1][2] < 0.1:
                            FitsMade.append(func)
                            continue
                    except:
                        pass
            Val = [FitsMade[i][1] for i in range(len(FitsMade))]
            for i in range(len(Val)):
                for j in range(len(Val)):
                    try:
                        if abs(Val[i][1]-Val[i][1])<5 and i != j:
                                if Val[i][2]<Val[j][2]:
                                    del Val[j]
                                else:
                                    del Val[i]
                    except:
                        pass
            print(Val)
            print(len(Val))
            print(len(FitsMade))
            print(FitsMade)
            xlist = np.linspace(self.xval[0], self.xval[-1], len(self.xval)*10)
            func = lambda x, a, mu, sigma: a*np.exp(-(x - mu)**2/(2*sigma**2))
            for i in range(len(Val)):
                ylist = np.array([func(x, Val[i][0], Val[i][1], Val[i][2]) for x in xlist])
                plt.plot(xlist, ylist, '-', label = f"Peak {i+1}")
            plt.plot(self.xval, self.yval, '.', label = "Data", markersize=0.5)
            plt.show()
import os
PATH1 = os.path.join("/Users/andreasevensen/Desktop/XrayDiffraction", "AG.xyd")
def Parser(Path):
    """Parser function provides the parsered data provided from a .xyd file. This method requires that the data
    is strictly ordered"""
    try:
        with open(Path, 'r') as file:
            Data = file.readlines()
        Xlist = []
        Ylist = []
        for i in range(len(Data)):
            Values = Data[i].split(' ')
            val2 = Values[-1].replace("\n", '')#Remove a newline and replace by nothing
            Xlist.append(float(Values[0]))
            Ylist.append(float(val2))
        return np.array(Xlist), np.array(Ylist)
    except:
        raise Exception("[Parser]: Cant find the input")
val = Parser(PATH1)
Test = Autoreg(val[0], val[1], Fit = "Gaussian")
