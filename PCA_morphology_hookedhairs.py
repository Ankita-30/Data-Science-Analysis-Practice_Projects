## load data in pandas ##
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn import decomposition
import matplotlib.pyplot as plt
import matplotlib

##without shape##

##read csv file sheet##

## N-Stress##
xl = pd.ExcelFile(r"/Users/ankita/Desktop/DataAnalysis/RGB/Procrustes/Re-analysis/Peter_Reanalysis/Data_Compile_AP_final_1.xlsx")
path=(r"/Users/ankita/Desktop/DataAnalysis/RGB/Procrustes/Re-analysis/Peter_Reanalysis/Plots_reanalysis")

def PCA_3D(xl,path):

    #drop columns#
    PCA_N= xl.parse('Nstress_violinplot')
    PCA_N = PCA_N.drop(PCA_N.columns[[4, 5, 6,7,8,9,10,11]], axis=1)

    #add label column##
    PCA_N=PCA_N.assign(Group=1)

    ## change column name ##
    PCA_N.columns=['Area','Perimeter','Length','PD','Group']


    ## P-Stress ##
    
    #drop columns#
    PCA_P= xl.parse('Pstress_violinplot')
    PCA_P = PCA_P.drop(PCA_P.columns[[4, 5, 6,7,8,9,10,11]], axis=1)

    #add label column##
    PCA_P=PCA_P.assign(Group=3)

    ## change column name ##
    PCA_P.columns=['Area','Perimeter','Length','PD','Group']


    ## Control ##
    
    #drop columns#
    PCA_C= xl.parse('Control_violinplot')
    PCA_C = PCA_C.drop(PCA_C.columns[[4, 5, 6,7,8,9,10,11]], axis=1)

    #add label column##
    PCA_C=PCA_C.assign(Group=2)

    ## change column name ##
    PCA_C.columns=['Area','Perimeter','Length','PD','Group']


    ## create the combined dataframe ##
    PCA=pd.concat([PCA_N, PCA_P, PCA_C], axis=0)
    PCA=PCA.dropna()


    ## scale the data ##
    features=PCA.columns[:-1]
    x = PCA.loc[:, features].values
    x = StandardScaler().fit_transform(x)

    ## label ##
    label=PCA.columns[-1]
    y = PCA.loc[:, label].values

    label = [1,2,3]
    colors = ['green','blue','red']


    ##PCA##
    pca = decomposition.PCA(n_components=3)
    principalComponents = pca.fit_transform(x)
    #principal_Df = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2'])

    ## plot PCA ##
    ## set  3D axis ##
    fig = plt.figure(1, figsize=(4, 3))
    plt.clf()

    ax = fig.add_subplot(111, projection="3d", elev=48, azim=134)
    ax.set_position([0, 0, 0.95, 1])
    plt.cla()

    ax.scatter(x[:, 0], x[:, 1], x[:, 2], c=y, cmap=matplotlib.colors.ListedColormap(colors))

    ax.w_xaxis.set_ticklabels([])
    ax.w_yaxis.set_ticklabels([])
    ax.w_zaxis.set_ticklabels([])

    ax.set_xlabel('PC 1')
    ax.set_ylabel('PC 2')
    ax.set_zlabel('PC 3')

    plt.show()
    plt.savefig(path)
    
    return()

PCA_3D(xl,path)