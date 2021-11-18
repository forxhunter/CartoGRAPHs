
########################################################################################
#
# This python file is part of the Project "cartoGRAPHs"
# for  E M B E D D I N G & P L O T T I N G  2D + 3D 
#
########################################################################################

import plotly
import plotly.graph_objs as pgo
import umap.umap_ as umap

from sklearn.manifold import TSNE
from sklearn.manifold import MDS
from sklearn import preprocessing

import numpy as np 
from numpy import pi, cos, sin, arccos, arange

import math 
import matplotlib.pyplot as plt

########################################################################################




# -------------------------------------------------------------------------------------
# A N N O T A T I O N S + L A B E L S 
# -------------------------------------------------------------------------------------

def annotation_kmeansclustering(kmeans, centrs, mode):
   
    # number of genes in each cluster ( used for annotation )
    d_clus_genecount = dict(collections.Counter(kmeans.labels_))
    d_clus_genecount_sort = dict(collections.OrderedDict(sorted(d_clus_genecount.items())))
    l_clus_genecount = list(d_clus_genecount_sort.values())

    # Centers for clusters ( used for annotation )
    x=[]
    y=[]
    z=[]
    for i in centrs:
        x.append(i[0])
        y.append(i[1])
        z.append(i[2])
        
    if mode == 'light':
        annotations = []
        for i in range(len(x)):
            annot = dict(
                                x=x[i],
                                y=y[i],
                                z=z[i],
                                showarrow=True,
                                text=f'Cluster: {str(i+1)} <br> total: {str(l_clus_genecount[i])}', 
                                font=dict(
                                    color="dimgrey",
                                    size=8),
                                xanchor="right",
                                ay=-20,
                                ax=-20,
                                opacity=0.5,
                                arrowhead=0,
                                arrowwidth=0.5,
                                arrowcolor="dimgrey"
                                )
            i=+1
            annotations.append(annot)
        return annotations

    elif mode == 'dark':
        annotations = []
        for i in range(len(x)):
            annot = dict(
                                x=x[i],
                                y=y[i],
                                z=z[i],
                                showarrow=True,
                                text=f'Cluster: {str(i+1)} <br> total: {str(l_clus_genecount[i])}',
                                font=dict(
                                    color="lightgrey",
                                    size=8),
                                xanchor="right",
                                ay=-20,
                                ax=-20,
                                opacity=0.5,
                                arrowhead=0,
                                arrowwidth=0.5,
                                arrowcolor="lightgrey")
            i=+1
            annotations.append(annot)
        return annotations
        
    else: 
        print('Please choose mode by setting mode="light" or "dark".')
        
        
        
def cluster_annotation(d_clusterid_coords, d_genes_per_cluster, mode = 'light'):
    ''' 
    Add Anntation of clusters to 3D plot.
    Input:
    - d_clusterid_coords = dictionary with cluster id and x,y,z coordinates of cluster center.
    - d_genes_per_cluster = dictionary with cluster id and genes counted per cluster 
    - mode = mode of plot (i.e. 'light', 'dark')
    
    Return Annotations for each cluster.
    '''    
    
    l_clus_genecount = list(d_genes_per_cluster.values())

    x=[]
    y=[]
    z=[]
    for i in d_clusterid_coords.values():
        x.append(i[0])
        y.append(i[1])
        z.append(i[2])

    if mode == 'light':
        annotations = []
        for i in range(len(x)):
            annot = dict(
                                x=x[i],
                                y=y[i],
                                z=z[i],
                                showarrow=True,
                                text=f'Cluster: {str(i+1)} <br> total: {str(l_clus_genecount[i])}', 
                                font=dict(
                                    color="dimgrey",
                                    size=8),
                                xanchor="right",
                                ay=-100,
                                ax=-100,
                                opacity=0.5,
                                arrowhead=0,
                                arrowwidth=0.5,
                                arrowcolor="dimgrey"
                                )
            i=+1
            annotations.append(annot)
        return annotations

    elif mode == 'dark':
        annotations = []
        for i in range(len(x)):
            annot = dict(
                                x=x[i],
                                y=y[i],
                                z=z[i],
                                showarrow=True,
                                text=f'Cluster: {str(i+1)} <br> total: {str(l_clus_genecount[i])}',
                                font=dict(
                                    color="lightgrey",
                                    size=8),
                                xanchor="right",
                                ay=-100,
                                ax=-100,
                                opacity=0.5,
                                arrowhead=0,
                                arrowwidth=0.5,
                                arrowcolor="lightgrey")
            i=+1
            annotations.append(annot)
        return annotations
        
    else: 
        print('Please choose mode by setting mode="light" or "dark".')

    

def genes_annotation(posG_genes, d_genes, mode = 'light'):
    '''
    Add Anntation of genes to 3D plot.
    Input:
    - posG_genes = dictionary with node id and x,y,z coordinates.
    - d_genes = dictionary with node id as keys and symbol (gene symbol) as values. Same order as posG_genes
    - mode of plot (i.e. 'light', 'dark')
    
    Return Annotations for each cluster.
    ''' 
    
    gene_sym = list(d_genes.values())
    
    x = []
    y = []
    z = []
    for k,v in posG_genes.items():
        x.append(v[0])
        y.append(v[1])
        z.append(v[2])

    if mode == 'light':
        annotations = []
        for i in range(len(x)):
            annot = dict(
                                    x=x[i],
                                    y=y[i],
                                    z=z[i],
                                    showarrow=True,
                                    text=f'Gene: {gene_sym[i]}',                            
                                    font=dict(
                                        color="dimgrey",
                                        size=10),
                                    xanchor="right",
                                    ay=-10,
                                    ax=-10,
                                    opacity=0.5,
                                    arrowhead=0,
                                    arrowwidth=0.5,
                                    arrowcolor="dimgrey")
            i=+1
            annotations.append(annot)
        return annotations

    elif mode == 'dark':
        annotations = []
        for i in range(len(x)):
            annot = dict(
                                    x=x[i],
                                    y=y[i],
                                    z=z[i],
                                    showarrow=True,
                                    text=f'Gene: {gene_sym[i]}',
                                    font=dict(
                                        color="white",
                                        size=10),
                                    xanchor="right",
                                    ay=-10,
                                    ax=-10,
                                    opacity=0.5,
                                    arrowhead=0,
                                    arrowwidth=0.5,
                                    arrowcolor="lightgrey")
            i=+1
            annotations.append(annot)
        return annotations

    else: 
        print('Please choose mode by setting mode="light" or "dark".')

        
        
def annotation_disease(position_annot, disease_names, disease_colors, mode):
   
    # number of genes in each cluster ( used for annotation )

    if mode == 'light':
        annotations = []
        for i in range(len(disease_names)):
            annot = dict(
                                x=position_annot[i][0],
                                y=position_annot[i][1],
                                z=position_annot[i][2],
                                showarrow=True,
                                text=disease_names[i], 
                                font=dict(
                                    color=disease_colors[i],
                                    size=14),
                                xanchor="right",
                                ay=0,
                                ax=0,
                                opacity=1,
                                arrowhead=0,
                                arrowwidth=0.5,
                                arrowcolor="dimgrey"
                                )
            i=+1
            annotations.append(annot)
        return annotations

    elif mode == 'dark':
        annotations = []
        for i in range(len(disease_names)):
            annot = dict(
                                x=position_annot[i][0],
                                y=position_annot[i][1],
                                z=position_annot[i][2],
                                showarrow=True,
                                text=disease_names[i],
                                font=dict(
                                    color=disease_colors[i],
                                    size=14),
                                xanchor="right",
                                ay=0,
                                ax=0,
                                opacity=1,
                                arrowhead=0,
                                arrowwidth=0.5,
                                arrowcolor="lightgrey")
            i=+1
            annotations.append(annot)
        return annotations
        
    else: 
        print('Please choose mode by setting mode="light" or "dark".')

        
########################################################################################

# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
#
#      ######     #######
#    ##     ##    ##    ##
#           ##    ##     ## 
#          ##     ##     ##
#        ##       ##     ##
#      ##         ##     ##
#    ##           ##    ##
#    ##########   #######
#
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------
# E M B E D D I N G 
# -------------------------------------------------------------------------------------


def embed_tsne_2D(Matrix, prplxty, density, l_rate, steps, metric = 'precomputed'):
    '''
    Dimensionality reduction from Matrix using t-SNE.
    Return dict (keys: node IDs, values: x,y).
    ''' 
    
    tsne = TSNE(n_components = 2, random_state = 0, perplexity = prplxty, metric = metric, init='pca',
                     early_exaggeration = density,  learning_rate = l_rate ,n_iter = steps,
                     square_distances=True)
    
    embed = tsne.fit_transform(Matrix)
    
    return embed



def embed_umap_2D(Matrix, n_neigh, spre, m_dist, metric='cosine', learn_rate = 1, n_ep = None):
    '''
    Dimensionality reduction from Matrix using UMAP.
    Return dict (keys: node IDs, values: x,y).
    ''' 
    n_comp = 2 

    U = umap.UMAP(
        n_neighbors = n_neigh,
        spread = spre,
        min_dist = m_dist,
        n_components = n_comp,
        metric = metric, 
        random_state=42,
        learning_rate = learn_rate, 
        n_epochs = n_ep)
    
    embed = U.fit_transform(Matrix)
    
    return embed


def get_posG_2D(l_nodes, embed):
    '''
    Get 2D coordinates for each node.
    Return dict with node: x,y coordinates.
    '''
    
    posG = {}
    cc = 0
    for entz in l_nodes:
        posG[entz] = (embed[cc,0],embed[cc,1])
        cc += 1

    return posG


def get_posG_2D_norm(G, DM, embed, r_scalingfactor = 1.2):
    '''
    Generate coordinates from embedding. 
    Input:
    - G = Graph
    - DM = matrix; index and columns must be same as G.nodes
    - embed = embedding from e.g. tSNE , UMAP ,... 
    
    Return dictionary with nodes as keys and coordinates as values in 3D normed. 
    '''
    
    genes = []
    for i in DM.index:
        if str(i) in G.nodes() or int(i) in G.nodes():
            genes.append(str(i))

    genes_rest = [] 
    for i in G.nodes():
        if i not in genes:
            genes_rest.append(str(i))

    #print(len(genes))
    #print(len(genes_rest))
        
    posG = {}
    cc = 0
    for entz in genes:
        posG[entz] = (embed[cc,0],embed[cc,1])
        cc += 1

    #--------------------------------------------------------------
    # REST (if genes = G.nodes then rest will be ignored / empty)
    
    # generate circle coordinates for rest genes (without e.g. GO term or Disease Annotation)
    t = np.random.uniform(0,2*np.pi,len(genes_rest))
    
    xx=[]
    yy=[]
    for i in posG.values():
        xx.append(i[0])
        yy.append(i[1])
    
    cx = np.mean(xx)
    cy = np.mean(yy)

    xm, ym = max(posG.values())
    r = (math.sqrt((xm-cx)**2 + (ym-cy)**2))*r_scalingfactor #*1.05 # multiplying with 1.05 makes cirle larger to avoid "outsider nodes/genes"
        
    x = r*np.cos(t)
    y = r*np.sin(t)
    rest = []
    for i,j in zip(x,y):
            rest.append((i,j))

    posG_rest = dict(zip(genes_rest, rest))

    posG_all = {**posG, **posG_rest}
    
    #G_nodes_str = [str(i) for i in list(G.nodes())]
    posG_complete = {key:posG_all[key] for key in list(G.nodes())}

    # normalize coordinates 
    x_list = []
    y_list = []
    for k,v in posG_complete.items():
        x_list.append(v[0])
        y_list.append(v[1])

    xx_norm = preprocessing.minmax_scale(x_list, feature_range=(0, 1), axis=0, copy=True)
    yy_norm = preprocessing.minmax_scale(y_list, feature_range=(0, 1), axis=0, copy=True)

    xx_norm_final=[]
    for i in xx_norm:
        xx_norm_final.append(round(i,10))

    yy_norm_final=[]
    for i in yy_norm:
        yy_norm_final.append(round(i,10))

    posG_complete_norm = dict(zip(list(G.nodes()),zip(xx_norm_final,yy_norm_final)))
    
    return posG_complete_norm




# -------------------------------------------------------------------------------------
# L A B E L S 
# -------------------------------------------------------------------------------------

def labels2D(posG, feature_dict):
    '''
    Create Node Labels, based on a dict of coordinates (keys:node ID, values: x,y)
    Return new dict of node iDs and features for each node.
    '''

    labels = {} 
    c = 0
    for node, xy in sorted(posG.items(), key = lambda x: x[1][0]):
        labels[node] = ([node,feature_dict[node][0],feature_dict[node][1],feature_dict[node][2],feature_dict[node][3]])   
        c+=1
        
    return labels


def position_labels(posG, move_x, move_y):
    '''
    Create label position of coordinates dict.
    Return new dict with label positions. 
    '''    
    
    posG_labels = {}
    for key,val in posG.items():
        xx = val[0] + move_x
        yy = val[1] + move_y
        posG_labels[key] = (xx,yy)
        
    return posG_labels


# -------------------------------------------------------------------------------------
# P L O T T I N G 
# -------------------------------------------------------------------------------------

def get_trace_nodes_2D(posG, info_list, color_list, size, linewidth=0.25, opac = 0.8):
    '''
    Get trace of nodes for plotting in 2D. 
    Input: 
    - G = Graph
    - posG = dictionary with nodes as keys and coordinates as values.
    - color_list = list of colors obtained from any color function (see above sections).
    - opacity = transparency of edges e.g. 0.2
    
    Return a trace for plotly graph objects plot. 
    '''
    
    key_list=list(posG.keys())
    trace = pgo.Scatter(x=[posG[key_list[i]][0] for i in range(len(key_list))],
                           y=[posG[key_list[i]][1] for i in range(len(key_list))],
                           mode = 'markers',
                           text = info_list,
                           hoverinfo = 'text',
                           #textposition='middle center',
                           marker = dict(
                color = color_list,
                size = size,
                symbol = 'circle',
                line = dict(width = linewidth,
                        color = 'dimgrey'),
                opacity = opac
            ),
        )
    
    return trace



def color_edges_from_nodelist_specific(G, l_nodes, color):
    '''
    Color (highlight) edges from specific node list exclusively.
    Input:
    - G = Graph 
    - l_nodes = list of nodes 
    - color = string; color to hightlight
    
    Return edge list for selected edges IF BOTH nodes are in l_nodes. 
    '''
    
    edge_lst = [(u,v)for u,v in G.edges(l_nodes) if u in l_nodes and v in l_nodes]

    d_col_edges = {}
    for e in edge_lst:
        d_col_edges[e]=color
    return d_col_edges



def get_trace_edges_2D(G, posG, color, opac = 0.2, linewidth = 0.2):
    '''
    Get trace of edges for plotting in 2D. 
    Input: 
    - G = Graph
    - posG = dictionary with nodes as keys and coordinates as values.
    - color = string; hex color
    - opacity = transparency of edges e.g. 0.2
    
    Return a trace for plotly graph objects plot. 
    '''
    
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = posG[edge[0]]
        x1, y1 = posG[edge[1]]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)
 
    trace_edges = pgo.Scatter(
                        x = edge_x, 
                        y = edge_y, 
                        mode = 'lines', hoverinfo='none',
                        line = dict(width = linewidth, color = color),
                        opacity = opac
                )
    
    return trace_edges


def get_trace_edges_specific2D(d_edges_col, posG, linew = 0.75, opac=0.1):

    edge_x = []
    edge_y = []
    
    for edge, col in d_edges_col.items():
            x0, y0 = posG[edge[0]]
            x1, y1 = posG[edge[1]]
            edge_x.append(x0)
            edge_x.append(x1)
            edge_x.append(None)
            edge_y.append(y0)
            edge_y.append(y1)
            edge_y.append(None)
            
    cols = list(d_edges_col.values())[0]
    
    trace_edges = pgo.Scatter(
                        x = edge_x, 
                        y = edge_y, 
                        mode = 'lines', hoverinfo='none',
                        line = dict(width = linew, color = cols),
                        opacity = opac
                )
    
    return trace_edges



def get_trace_edges_from_nodelist2D(G, l_nodes, posG, color, linew = 0.75, opac=0.1):
    '''
    Get trace of edges for plotting in 3D only for specific edges. 
    Input: 
    - G = Graph
    - posG = dictionary with nodes as keys and coordinates as values.
    - color = string; specific color to highlight specific edges; hex color
    
    Return a trace of specific edges. 
    '''
    l_spec_edges = [(u,v) for u,v in G.edges(l_nodes) if u in l_nodes and v in l_nodes]
   
    edge_x = []
    edge_y = []
    
    for edge in l_spec_edges:
            x0, y0 = posG[edge[0]]
            x1, y1 = posG[edge[1]]
            edge_x.append(x0)
            edge_x.append(x1)
            edge_x.append(None)
            edge_y.append(y0)
            edge_y.append(y1)
            edge_y.append(None)
            

    trace_edges = pgo.Scatter(
                        x = edge_x, 
                        y = edge_y, 
                        mode = 'lines', hoverinfo='none',
                        line = dict(width = linew, color = color),
                        opacity = opac
                )
    
    return trace_edges



def plot_2D(data,path,fname):
    '''
    Create a 2D plot from traces using plotly.
    Input: 
    - data = list of traces
    - filename = string
    
    Return plot in 2D and file, saved as png.
    '''

    fig = pgo.Figure()
    
    for i in data:
        fig.add_trace(i)
        
    fig.update_layout(template= 'plotly_white', 
                      showlegend=False, width=1200, height=1200,
                          scene=dict(
                              xaxis_title='',
                              yaxis_title='',
                              xaxis=dict(nticks=0,tickfont=dict(
                                    color='white')),
                              yaxis=dict(nticks=0,tickfont=dict(
                                    color='white')),
                        ))    
    fig.update_xaxes(visible=False)
    fig.update_yaxes(visible=False)
    
    # --- show figure ---
    #py.iplot(fig)
    
    # --- get html file ---  
    fig.write_html(path+fname+'.html')
    
    # --- get screenshot image (png) from html --- 
    #hti = Html2Image(output_path=path)
    #hti.screenshot(html_file = path+fname+'.html', save_as = fname+'.png')
    
    #not working with large file / time ! 
    #fig.write_image(fname+'.png') 
    
    return plotly.offline.plot(fig, filename = path+fname+'.html', auto_open=True)

        
########################################################################################

# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
#      ######     #######
#    ##     ##    ##    ##
#           ##    ##     ## 
#      #####      ##     ##
#           ##    ##     ##
#    ##     ##    ##    ##
#     ######      #######
#    
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------
# E M B E D D I N G 
# -------------------------------------------------------------------------------------

def embed_tsne_3D(Matrix, prplxty, density, l_rate, n_iter, metric = 'cosine'):
    '''
    Dimensionality reduction from Matrix (t-SNE).
    Return dict (keys: node IDs, values: x,y,z).
    '''
    
    tsne3d = TSNE(n_components = 3, random_state = 0, perplexity = prplxty,
                     early_exaggeration = density,  learning_rate = l_rate, n_iter = n_iter, metric = metric,
                 square_distances=True)
    embed = tsne3d.fit_transform(Matrix)

    return embed 


def embed_umap_3D(Matrix, n_neighbors, spread, min_dist, metric='cosine', learn_rate = 1, n_ep = None):
    '''
    Dimensionality reduction from Matrix (UMAP).
    Return dict (keys: node IDs, values: x,y,z).
    '''

    n_components = 3 # for 3D

    U_3d = umap.UMAP(
        n_neighbors = n_neighbors,
        spread = spread,
        min_dist = min_dist,
        n_components = n_components,
        metric = metric,
        random_state=42,
        learning_rate = learn_rate, 
        n_epochs = n_ep)
    embed = U_3d.fit_transform(Matrix)
    
    return embed


def get_posG_3D(l_genes, embed):
    '''
    Generate coordinates from embedding. 
    Input:
    - l_genes = list of genes
    - embed = embedding from e.g. tSNE , UMAP ,... 
    
    Return dictionary with nodes as keys and coordinates as values in 3D. 
    '''
    
    posG = {}
    cc = 0
    for entz in l_genes:
        posG[entz] = (embed[cc,0],embed[cc,1],embed[cc,2])
        cc += 1
    
    return posG


def get_posG_3D_norm(G, DM, embed, r_scalingfactor=1.05):
    '''
    Generate coordinates from embedding. 
    Input:
    - G = Graph
    - DM = matrix 
    - embed = embedding from e.g. tSNE , UMAP ,... 
    
    Return dictionary with nodes as keys and coordinates as values in 3D normed. 
    '''

    genes = []
    for i in DM.index:
        if str(i) in G.nodes() or int(i) in G.nodes():
            genes.append(i)

    genes_rest = [] 
    for i in G.nodes():
        if i not in genes:
            genes_rest.append(i)
            
    posG_3Dumap = {}
    cc = 0
    for entz in genes:
        posG_3Dumap[entz] = (embed[cc,0],embed[cc,1],embed[cc,2])
        cc += 1

    #--------------------------------------------------------------
    # REST (if genes = G.nodes then rest will be ignored / empty)
    
    # center for sphere to arrange rest gene-datapoints
    xx=[]
    yy=[]
    zz=[]
    for i in posG_3Dumap.values():
        xx.append(i[0])
        yy.append(i[1])
        zz.append(i[2]) 

    cx = sum(xx)/len(genes)
    cy = sum(yy)/len(genes)
    cz = sum(zz)/len(genes)

    # generate spherical coordinates for rest genes (without e.g. GO term or Disease Annotation)
    indices = arange(0, len(genes_rest))
    phi = arccos(1 - 2*indices/len(genes_rest)) # 2* --> for both halfs of sphere (upper+lower)
    theta = pi * (1 + 5**0.5) * indices

    xm, ym, zm = max(posG_3Dumap.values())
    r = (math.sqrt((cx - xm)**2 + (cy - ym)**2 + (cz - zm)**2))*r_scalingfactor # +10 > ensure colored nodes within sphere
    x, y, z = cx+r*cos(theta) * sin(phi),cy+r*sin(theta) * sin(phi), cz+r*cos(phi)

    rest_points = []
    for i,j,k in zip(x,y,z):
        rest_points.append((i,j,k))

    posG_rest = dict(zip(genes_rest, rest_points))

    posG_all = {**posG_3Dumap, **posG_rest}
    posG_3D_complete_umap = {key:posG_all[key] for key in G.nodes()}

    # normalize coordinates 
    x_list3D = []
    y_list3D = []
    z_list3D = []
    for k,v in posG_3D_complete_umap.items():
        x_list3D.append(v[0])
        y_list3D.append(v[1])
        z_list3D.append(v[2])

    xx_norm3D = preprocessing.minmax_scale(x_list3D, feature_range=(0, 1), axis=0, copy=True)
    yy_norm3D = preprocessing.minmax_scale(y_list3D, feature_range=(0, 1), axis=0, copy=True)
    zz_norm3D = preprocessing.minmax_scale(z_list3D, feature_range=(0, 1), axis=0, copy=True)

    xx_norm3D_final=[]
    for i in xx_norm3D:
        xx_norm3D_final.append(round(i,10))

    yy_norm3D_final=[]
    for i in yy_norm3D:
        yy_norm3D_final.append(round(i,10))

    zz_norm3D_final=[]
    for i in zz_norm3D:
        zz_norm3D_final.append(round(i,10)) 

    posG_3D_complete_umap_norm = dict(zip(list(G.nodes()), zip(xx_norm3D_final,yy_norm3D_final,zz_norm3D_final)))
    
    return posG_3D_complete_umap_norm



def embed_umap_sphere(Matrix, n_neighbors, spread, min_dist):
    ''' 
    Generate spherical embedding of nodes in matrix input using UMAP.
    Input: 
    - Matrix = Feature Matrix with either all or specific  nodes (rows) and features (columns) or symmetric (nodes = rows and columns)
    - n_neighbors/spread/min_dist = floats; UMAP parameters.
    - metric = string; e.g. havervine, euclidean, cosine ,.. 
    
    Return sphere embedding. 
    '''
    
    model = umap.UMAP(
        n_neighbors = n_neighbors, 
        spread = spread,
        min_dist = min_dist,
        output_metric = 'haversine',
        random_state=42)
    sphere_mapper = model.fit(Matrix)

    return sphere_mapper



def get_posG_sphere_norm(G, DM, sphere_mapper, d_param, radius_rest_genes = 20):
    '''
    Generate coordinates from embedding. 
    Input:
    - G = Graph 
    - l_genes = list of node IDs, either specific or all nodes in the graph 
    - sphere_mapper = embedding from UMAP spherical embedding 
    - d_param = dictionary with nodes as keys and assigned radius as values 
    - radius_rest_genes = int; radius in case of genes e.g. not function associated if genes not all G.nodes()
    
    Return dictionary with nodes as keys and coordinates as values in 3D. 
    '''
    
    x = np.sin(sphere_mapper.embedding_[:, 0]) * np.cos(sphere_mapper.embedding_[:, 1])
    y = np.sin(sphere_mapper.embedding_[:, 0]) * np.sin(sphere_mapper.embedding_[:, 1])
    z = np.cos(sphere_mapper.embedding_[:, 0])
    
    genes = []
    for i in DM.index:
        if str(i) in G.nodes() or int(i) in G.nodes():
            genes.append(i)

    genes_rest = [] 
    for i in G.nodes():
        if i not in genes:
            genes_rest.append(i)
            
    posG_3Dsphere = {}
    cc = 0
    for entz in genes:
        posG_3Dsphere[entz] = (x[cc],y[cc], z[cc])
        cc += 1

    posG_3Dsphere_radius = {}
    for node,rad in d_param.items():
        for k,v in posG_3Dsphere.items():
            if k == node:
                posG_3Dsphere_radius[k] = (v[0]*rad, v[1]*rad, v[2]*rad)
 
    # generate spherical coordinates for rest genes (without e.g. GO term or Disease Annotation)
    indices = arange(0, len(genes_rest))
    phi = arccos(1 - 2*indices/len(genes_rest))
    theta = pi * (1 + 5**0.5) * indices

    r_rest = radius_rest_genes # radius for rest genes (e.g. if functional layout)
    x, y, z = r_rest*cos(theta) * sin(phi), r_rest*sin(theta) * sin(phi), r_rest*cos(phi)

    rest_points = []
    for i,j,k in zip(x,y,z):
        rest_points.append((i,j,k))

    posG_rest = dict(zip(genes_rest, rest_points))

    posG_all = {**posG_3Dsphere_radius, **posG_rest}
    posG_complete_sphere = {key:posG_all[key] for key in G.nodes()}

    # normalize coordinates 
    x_list = []
    y_list = []
    z_list = []
    for k,v in posG_complete_sphere.items():
        x_list.append(v[0])
        y_list.append(v[1])
        z_list.append(v[2])

    xx_norm = preprocessing.minmax_scale(x_list, feature_range=(0, 1), axis=0, copy=True)
    yy_norm = preprocessing.minmax_scale(y_list, feature_range=(0, 1), axis=0, copy=True)
    zz_norm = preprocessing.minmax_scale(z_list, feature_range=(0, 1), axis=0, copy=True)

    posG_complete_sphere_norm = dict(zip(list(G.nodes()), zip(xx_norm,yy_norm,zz_norm)))
    
    return posG_complete_sphere_norm



# -------------------------------------------------------------------------------------
# P L O T T I N G 
# -------------------------------------------------------------------------------------


def get_trace_nodes_3D(posG, info_list, color_list, size, linewidth=0.25, opac = 0.8):
    '''
    Get trace of nodes for plotting in 3D. 
    Input: 
    - posG = dictionary with nodes as keys and coordinates as values.
    - info_list = hover information for each node, e.g. a list sorted according to the initial graph/posG keys
    - color_list = string; hex color
    - opac = transparency of edges e.g. 0.2
    
    Return a trace for plotly graph objects plot. 
    '''
    
    key_list=list(posG.keys())
    trace = pgo.Scatter3d(x=[posG[key_list[i]][0] for i in range(len(key_list))],
                           y=[posG[key_list[i]][1] for i in range(len(key_list))],
                           z=[posG[key_list[i]][2] for i in range(len(key_list))],
                           mode = 'markers',
                           text = info_list,
                           hoverinfo = 'text',
                           #textposition='middle center',
                           marker = dict(
                color = color_list,
                size = size,
                symbol = 'circle',
                line = dict(width = linewidth,
                        color = 'dimgrey'),
                opacity = opac
            ),
        )
    
    return trace


def get_trace_edges_3D(G, posG, color, opac = 0.2, linewidth=0.2):
    '''
    Get trace of edges for plotting in 3D. 
    Input: 
    - G = Graph
    - posG = dictionary with nodes as keys and coordinates as values.
    - color = string; hex color
    - opac = transparency of edges e.g. 0.2
    
    Return a trace for plotly graph objects plot. 
    '''
    
    edge_x = []
    edge_y = []
    edge_z = []
    for edge in G.edges():
            x0, y0, z0 = posG[edge[0]]
            x1, y1, z1 = posG[edge[1]]
            edge_x.append(x0)
            edge_x.append(x1)
            edge_x.append(None)
            edge_y.append(y0)
            edge_y.append(y1)
            edge_y.append(None)
            edge_z.append(z0)
            edge_z.append(z1)
            edge_z.append(None)

    trace_edges = pgo.Scatter3d(
                                x = edge_x, 
                                y = edge_y, 
                                z = edge_z,
                                mode = 'lines', hoverinfo='none',
                                line = dict(width = linewidth, color = color),
                                opacity = opac
                        )

    return trace_edges



def get_trace_edges_from_nodelist3D(G, l_genes, posG, color, linew = 0.75, opac=0.1):
    '''
    Get trace of edges for plotting in 3D only for specific edges. 
    Input: 
    - G = Graph
    - posG = dictionary with nodes as keys and coordinates as values.
    - color = string; specific color to highlight specific edges; hex color
    
    Return a trace of specific edges. 
    '''
    l_spec_edges = [(u,v)for u,v in G.edges(l_genes) if u in l_genes and v in l_genes]
    
    edge_x = []
    edge_y = []
    edge_z = []
    for edge in l_spec_edges:
            x0, y0,z0 = posG[edge[0]]
            x1, y1,z1 = posG[edge[1]]
            edge_x.append(x0)
            edge_x.append(x1)
            edge_x.append(None)
            edge_y.append(y0)
            edge_y.append(y1)
            edge_y.append(None)
            edge_z.append(z0)
            edge_z.append(z1)
            edge_z.append(None)
            
    trace_edges = pgo.Scatter3d(
                        x = edge_x, 
                        y = edge_y, 
                        z = edge_z,
                        mode = 'lines', hoverinfo='none',
                        line = dict(width = linew, color = color),
                        opacity = opac
                )
    return trace_edges


def get_trace_edges_specific3D(d_edges_col, posG, linew = 0.75, opac=0.1):

    edge_x = []
    edge_y = []
    edge_z = []
    for edge, col in d_edges_col.items():
            x0, y0,z0 = posG[edge[0]]
            x1, y1,z1 = posG[edge[1]]
            edge_x.append(x0)
            edge_x.append(x1)
            edge_x.append(None)
            edge_y.append(y0)
            edge_y.append(y1)
            edge_y.append(None)
            edge_z.append(z0)
            edge_z.append(z1)
            edge_z.append(None)
            
    color = list(d_edges_col.values())[0]
    
    trace_edges = pgo.Scatter3d(
                        x = edge_x, 
                        y = edge_y, 
                        z = edge_z,
                        mode = 'lines', hoverinfo='none',
                        line = dict(width = linew, color = color),
                        opacity = opac
                )
    
    return trace_edges


def get_trace_edges_landscape(x,y,z0,z):
    '''
    Create trace of vertical connecting edges in between node z0 and node z=parameter (e.g.disease count).
    Return trace with edges.
    '''
    
    Xe = []
    for u in x:
        Xe += [u,u,None]

    Ye = []   
    for v in y:
        Ye += [v,v,None]  

    Ze = []  
    for w in z0:
        for t in z:
            Ze += [w,t,None]
            
    trace_edge = pgo.Scatter3d(
        x = Xe, 
        y = Ye, 
        z = Ze,
        mode = 'lines', hoverinfo='none',
        line = dict(width = 3.0, color = 'darkgrey'),
        opacity = 0.5
    )

    return trace_edge


def plot_3D(data,path,fname, scheme='light',annotat=None):
    '''
    Create a 3D plot from traces using plotly.
    Input: 
    - data = list of traces
    - filename = string
    - scheme = 'light' or 'dark'
    - annotations = None or plotly annotations
    
    Return plot in 3D and file, saved as html.
    '''

    fig = pgo.Figure()
    
    for i in data:
        fig.add_trace(i)
      
    if scheme == 'dark' and annotat==None:
        fig.update_layout(template='plotly_dark', showlegend=False, autosize = True,
                          scene=dict(
                              xaxis_title='',
                              yaxis_title='',
                              zaxis_title='',
                              xaxis=dict(nticks=0,tickfont=dict(
                                    color='black')),
                              yaxis=dict(nticks=0,tickfont=dict(
                                    color='black')),
                              zaxis=dict(nticks=0,tickfont=dict(
                                    color='black')),
                            dragmode="turntable"
                        )) 
        
    elif scheme == 'dark':    
        fig.update_layout(template='plotly_dark', showlegend=False, autosize = True,
                                  scene=dict(
                                      xaxis_title='',
                                      yaxis_title='',
                                      zaxis_title='',
                                      xaxis=dict(nticks=0,tickfont=dict(
                                            color='black')),
                                      yaxis=dict(nticks=0,tickfont=dict(
                                            color='black')),
                                      zaxis=dict(nticks=0,tickfont=dict(
                                            color='black')),
                                    dragmode="turntable",
                                    annotations=annotat,
                                ))

    elif scheme == 'light' and annotat==None:
        fig.update_layout(template='plotly_white', showlegend=False, width=1200, height=1200,
                          scene=dict(
                              xaxis_title='',
                              yaxis_title='',
                              zaxis_title='',
                              xaxis=dict(nticks=0,tickfont=dict(
                                    color='white')),
                              yaxis=dict(nticks=0,tickfont=dict(
                                    color='white')),
                              zaxis=dict(nticks=0,tickfont=dict(
                                    color='white')),    
                            dragmode="turntable",
                        ))    
        
    elif scheme == 'light':
        fig.update_layout(template='plotly_white', showlegend=False, width=1200, height=1200,
                          scene=dict(
                              xaxis_title='',
                              yaxis_title='',
                              zaxis_title='',
                              xaxis=dict(nticks=0,tickfont=dict(
                                    color='white')),
                              yaxis=dict(nticks=0,tickfont=dict(
                                    color='white')),
                              zaxis=dict(nticks=0,tickfont=dict(
                                    color='white')),    
                            dragmode="turntable",
                            annotations = annotat
                        ))    

    fig.update_xaxes(visible=False)
    fig.update_yaxes(visible=False)
    
    # --- show figure ---
    #py.iplot(fig)
    
    # --- get html file ---  
    #fig.write_html(path+fname+'.html')
    
    return plotly.offline.plot(fig, filename = path+fname+'.html', auto_open=True)