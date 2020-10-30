# PhysicsNum
 Physics Numerical methods applied and used during the bachlelor degree in Physics at Lund University. Most notbly is the numerical approximation methods and similar.
 The code regression works upon least square methods, and weighted least square methods and have been verified. If an issue occurs when using this package, contact via GitHub for a fast solution.

# Simple test of the code:
```python
xlist1 = np.array([1,2,3,4,5,6,8,9,10])
ylist1 = np.array([2,3,4,7,8,6,5,4,3])
listx2 = np.linspace(-1, 15, 100)
Fitted = Gaussianfit(xlist1, ylist1)
fittedx = list(map(Fitted, listx2))
Data = GaussianFit(xlist1, ylist1)
data = Data.ComputeGausian(0, 9)
plt.plot(listx2, fittedx)
plt.plot(xlist1, ylist1, '.', label = "tested values")
plt.show()
```
Note that this is a poor descriptions of this potential. The following section was used in a bachlelor course:
```python
Thorium1 = load_spectrum('/Users/andreasevensen/Documents/GitHub/Fysc12/AlphaLab/20201007/Thorium.Spe')
Thorium = GaussianFit(Thorium1[0], Thorium1[1])
Thorium.Calibration(EnergyConvertion, CalibrationConstant / Center)
Thoriumpeak1 = Thorium.ComputeGaussian(2308, 2338)
Thoriumpeak2 = Thorium.ComputeGaussian(2345, 2379)
Thoriumpeak3 = Thorium.ComputeGaussian(2457, 2495)
Thoriumpeak4 = Thorium.ComputeGaussian(2605, 2675)
Thoriumpeak5 = Thorium.ComputeGaussian(2720, 2760)
Thoriumpeak6 = Thorium.ComputeGaussian(2938, 2975)
Thoriumpeak7 = Thorium.ComputeGaussian(3818, 3850)

print(Thorium.PeakValues)
print(Thorium.Area)
print(Thorium.Sigma)
Thorium.PlotData("Thorium Spectrum", "Energy [keV]", "Counts", xlim = 10000)
Sigmavalues = np.array(Thorium.Sigma)
FWHM = 2 * np.sqrt(2 * np.log(2)) * Sigmavalues
print(FWHM)
```
As visualized, the regression has potential in many areas.

# Contribute
Feel free to contribute to this code, it is found on github under the authors name.
