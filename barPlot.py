import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import os

def plotDM(rho,folderName,name,labels=['0','1'],title=''):
    
    data = np.real(rho)


    fig = plt.figure(figsize=plt.figaspect(0.4))

    ax = fig.add_subplot(1, 2, 1, projection='3d')
    

    lx = len(data[0])            # Work out matrix dimensions
    ly = len(data[:,0])

    column_names = lx
    row_names = ly



    xpos = np.arange(0,lx,1)    # Set up a mesh of positions
    ypos = np.arange(0,ly,1)
    xpos, ypos = np.meshgrid(xpos, ypos)

    xpos = xpos.flatten()   # Convert positions to 1D array
    ypos = ypos.flatten()
    zpos = np.zeros(lx*ly)

    dx = 0.5*np.ones_like(zpos)
    dy = dx.copy()
    dz = data.flatten()


    ax.bar3d(xpos,ypos,zpos, dx, dy, dz ) #color=cs

    ax.xaxis.set_major_locator(ticker.FixedLocator((xpos+0.25)))
    ax.xaxis.set_major_formatter(ticker.FixedFormatter((xpos)))

    ax.yaxis.set_major_locator(ticker.FixedLocator((ypos+0.25)))
    ax.yaxis.set_major_formatter(ticker.FixedFormatter((ypos)))

    ax.set_xticks([0.2,1.])
    ax.set_xticklabels(labels)
    ax.set_yticks([0.5,1.2])
    ax.set_yticklabels(labels)
    
    #ax.set_xlabel('n')
    #ax.set_ylabel('m')
    ax.set_zlim(-0.5, 1)
    ax.set_zlabel("Re $\\rho$")

    ax = fig.add_subplot(1, 2, 2, projection='3d')

    data = np.imag(rho)

    lx = len(data[0])            # Work out matrix dimensions
    ly = len(data[:,0])

    column_names = lx
    row_names = ly



    xpos = np.arange(0,lx,1)    # Set up a mesh of positions
    ypos = np.arange(0,ly,1)
    xpos, ypos = np.meshgrid(xpos, ypos)

    xpos = xpos.flatten()   # Convert positions to 1D array
    ypos = ypos.flatten()
    zpos = np.zeros(lx*ly)

    dx = 0.5*np.ones_like(zpos)
    dy = dx.copy()
    dz = data.flatten()

    ax.set_title('Manual y', y=1.0, x=0, pad=-5)
    plt.title(title)
    
    ax.bar3d(xpos,ypos,zpos, dx, dy, dz ) #color=cs

    ax.xaxis.set_major_locator(ticker.FixedLocator((xpos+0.25)))
    ax.xaxis.set_major_formatter(ticker.FixedFormatter((xpos)))

    ax.yaxis.set_major_locator(ticker.FixedLocator((ypos+0.25)))
    ax.yaxis.set_major_formatter(ticker.FixedFormatter((ypos)))


    ax.set_xticks([0.2,1.])
    ax.set_xticklabels(labels)
    ax.set_yticks([0.5,1.2])
    ax.set_yticklabels(labels)
    
    
    ax.set_zlim(-0.5, 1)
    ax.set_zlabel("Im $\\rho$")
    if not os.path.exists(folderName):
        os.makedirs(folderName)
    
    plt.savefig(f'{folderName}/{name}-DensityMatrix.pdf',bbox_inches="tight",pad_inches=0.3)