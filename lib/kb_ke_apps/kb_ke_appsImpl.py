# -*- coding: utf-8 -*-
#BEGIN_HEADER
import os

from kb_ke_apps.Utils.KnowledgeEngineAppsUtil import KnowledgeEngineAppsUtil
#END_HEADER


class kb_ke_apps:
    '''
    Module Name:
    kb_ke_apps

    Module Description:
    A KBase module: kb_ke_apps
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "1.0.0"
    GIT_URL = "https://github.com/Tianhao-Gu/kb_ke_apps.git"
    GIT_COMMIT_HASH = "c1d2807c8d85718ec51491a42aeb7bc41c170676"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.config = config
        self.config['SDK_CALLBACK_URL'] = os.environ['SDK_CALLBACK_URL']
        self.config['KB_AUTH_TOKEN'] = os.environ['KB_AUTH_TOKEN']
        #END_CONSTRUCTOR
        pass


    def run_hierarchical_cluster(self, ctx, params):
        """
        run_hierarchical_cluster: generates hierarchical clusters for Matrix data object
        :param params: instance of type "HierClusterParams" (Input of the
           run_hierarchical_cluster function matrix_ref: Matrix object
           reference workspace_name: the name of the workspace
           feature_set_suffix: suffix append to FeatureSet object name
           dist_threshold: the threshold to apply when forming flat clusters
           Optional arguments: dist_metric: The distance metric to use.
           Default set to 'euclidean'. The distance function can be
           ["braycurtis", "canberra", "chebyshev", "cityblock",
           "correlation", "cosine", "dice", "euclidean", "hamming",
           "jaccard", "kulsinski", "matching", "rogerstanimoto",
           "russellrao", "sokalmichener", "sokalsneath", "sqeuclidean",
           "yule"] Details refer to:
           https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.
           distance.pdist.html linkage_method: The linkage algorithm to use.
           Default set to 'ward'. The method can be ["single", "complete",
           "average", "weighted", "centroid", "median", "ward"] Details refer
           to:
           https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.
           hierarchy.linkage.html fcluster_criterion: The criterion to use in
           forming flat clusters. Default set to 'distance'. The criterion
           can be ["inconsistent", "distance", "maxclust"] Details refer to:
           https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.
           hierarchy.fcluster.html) -> structure: parameter "matrix_ref" of
           type "obj_ref" (An X/Y/Z style reference), parameter
           "workspace_name" of String, parameter "feature_set_suffix" of
           String, parameter "dist_threshold" of Double, parameter
           "dist_metric" of String, parameter "linkage_method" of String,
           parameter "fcluster_criterion" of String
        :returns: instance of type "HierClusterOutput" (Ouput of the
           run_hierarchical_cluster function feature_set_set_refs: a list of
           result FeatureSetSet object references report_name: report name
           generated by KBaseReport report_ref: report reference generated by
           KBaseReport) -> structure: parameter "feature_set_set_refs" of
           list of type "obj_ref" (An X/Y/Z style reference), parameter
           "report_name" of String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN run_hierarchical_cluster
        for key, value in params.iteritems():
            if isinstance(value, basestring):
                params[key] = value.strip()

        ke_apps_util = KnowledgeEngineAppsUtil(self.config)
        returnVal = ke_apps_util.run_hierarchical_cluster(params)
        #END run_hierarchical_cluster

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method run_hierarchical_cluster return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def run_kmeans_cluster(self, ctx, params):
        """
        run_kmeans_cluster: generates Kmeans clusters for Matrix data object
        :param params: instance of type "KmeansClusterParams" (Input of the
           run_kmeans_cluster function matrix_ref: Matrix object reference
           workspace_name: the name of the workspace cluster_set_suffix:
           suffix append to KBaseExperiments.ClusterSet object name k_num:
           number of clusters to form Optional arguments: dist_metric: The
           distance metric to use. Default set to 'euclidean'. The distance
           function can be ["braycurtis", "canberra", "chebyshev",
           "cityblock", "correlation", "cosine", "dice", "euclidean",
           "hamming", "jaccard", "kulsinski", "matching", "rogerstanimoto",
           "russellrao", "sokalmichener", "sokalsneath", "sqeuclidean",
           "yule"] Details refer to:
           https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.
           distance.pdist.html) -> structure: parameter "matrix_ref" of type
           "obj_ref" (An X/Y/Z style reference), parameter "workspace_name"
           of String, parameter "cluster_set_suffix" of String, parameter
           "k_num" of Long, parameter "dist_metric" of String
        :returns: instance of type "KmeansClusterOutput" (Ouput of the
           run_kmeans_cluster function cluster_set_ref:
           KBaseExperiments.ClusterSet object references report_name: report
           name generated by KBaseReport report_ref: report reference
           generated by KBaseReport) -> structure: parameter
           "cluster_set_ref" of type "obj_ref" (An X/Y/Z style reference),
           parameter "report_name" of String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN run_kmeans_cluster
        for key, value in params.iteritems():
            if isinstance(value, basestring):
                params[key] = value.strip()

        ke_apps_util = KnowledgeEngineAppsUtil(self.config)
        returnVal = ke_apps_util.run_kmeans_cluster(params)
        #END run_kmeans_cluster

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method run_kmeans_cluster return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
