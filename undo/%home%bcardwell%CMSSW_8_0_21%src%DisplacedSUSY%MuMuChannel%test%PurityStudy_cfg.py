Vim�UnDo� ہ���\<7N?���=��IL�}"�Z��   p   Tadd_channels (process, eventSelections, histograms, weights, scalingfactorproducers,   n   S                       Y'r(    _�                             ����                                                                                                                                                                                                                                                                                                                                                             Y'q     �                %process = cms.Process ('OSUAnalysis')5�_�                       ?    ����                                                                                                                                                                                                                                                                                                                                                             Y'q     �         �      V    'file:/store/user/bcardwell/MuMuSkim_17_02_03/DoubleMu_2016B/MuMuSkim/skim_0.root'5�_�                    '   $    ����                                                                                                                                                                                                                                                                                                                                                             Y'q     �   &   (   �      &    input = cms.untracked.int32 (1000)5�_�                    )        ����                                                                                                                                                                                                                                                                                                                            )           4   $       V   $    Y'q     �   (   )              1data_global_tag = '80X_dataRun2_2016SeptRepro_v3'   9mc_global_tag = '80X_mcRun2_asymptotic_2016_miniAODv2_v1'       Pprocess.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')   2from Configuration.AlCa.GlobalTag import GlobalTag   Cprocess.GlobalTag = GlobalTag(process.GlobalTag, mc_global_tag, '')   bif osusub.batchMode and (osusub.datasetLabel in types) and (types[osusub.datasetLabel] == "data"):   7    print "using global tag " + data_global_tag + "..."   I    process.GlobalTag = GlobalTag(process.GlobalTag, data_global_tag, '')   else:   5    print "using global tag " + mc_global_tag + "..."5�_�                    )        ����                                                                                                                                                                                                                                                                                                                            )           )   $       V   $    Y'q!     �   (   )           5�_�      	                     ����                                                                                                                                                                                                                                                                                                                            )           )   $       V   $    Y'q;     �         }      # suppress gen-matching erros5�_�      
           	   0       ����                                                                                                                                                                                                                                                                                                                            @          0          V       Y'qV     �   /   A   }      ;  electrons       =  cms.InputTag  ('slimmedElectrons',''),   J  genjets         =  cms.InputTag  ('slimmedGenJets',                 ''),   J  jets            =  cms.InputTag  ('slimmedJets',                    ''),   J  bjets           =  cms.InputTag  ('slimmedJets',                    ''),   6  generatorweights=  cms.InputTag  ('generator', ''),    J  mcparticles     =  cms.InputTag  ('packedGenParticles',             ''),   V  hardInteractionMcparticles  =  cms.InputTag  ('prunedGenParticles',             ''),   J  mets            =  cms.InputTag  ('slimmedMETs',                    ''),   J  muons           =  cms.InputTag  ('slimmedMuons',                   ''),   J  photons         =  cms.InputTag  ('slimmedPhotons',                 ''),   J  primaryvertexs  =  cms.InputTag  ('offlineSlimmedPrimaryVertices',  ''),   A  pileupinfos     =  cms.InputTag  ('slimmedAddPileupInfo',  ''),   J  beamspots       =  cms.InputTag  ('offlineBeamSpot',                ''),   ^  superclusters   =  cms.InputTag  ('reducedEgamma',                  'reducedSuperClusters'),   J  taus            =  cms.InputTag  ('slimmedTaus',                    ''),   R  triggers        =  cms.InputTag  ('TriggerResults',                 '',  'HLT'),   J  trigobjs        =  cms.InputTag  ('selectedPatTrigger',             ''),5�_�   	              
   J        ����                                                                                                                                                                                                                                                                                                                            J          V           V       Y'q]     �   I   J          >variableProducers.append('DisplacedSUSYEventVariableProducer')   2variableProducers.append('LifetimeWeightProducer')       weights = cms.VPSet(       cms.PSet (   9        inputCollections = cms.vstring("eventvariables"),   4        inputVariable = cms.string("lifetimeWeight")       ),   )       scalingfactorproducers = []        5�_�   
                 O        ����                                                                                                                                                                                                                                                                                                                            J          J           V       Y'qv     �   S   W   s       eventSelections = [Preselection]�   N   S   p      4from DisplacedSUSY.MuMuChannel.Preselection import *5�_�                    O       ����                                                                                                                                                                                                                                                                                                                            O          P                 Y'q�     �   N   P   u      /from DisplacedSUSY.Channel.JustTrigger import *�   N   Q   u      1from DisplacedSUSY.EEChannel.JustTrigger import *   :from DisplacedSUSY.EEChannel.PreselectionMinusIso import *5�_�                    ^        ����                                                                                                                                                                                                                                                                                                                            O          P                 Y'q�     �   ]   ^          ]from OSUT3Analysis.Configuration.histogramDefinitions import JetHistograms, MuonJetHistograms5�_�                    f        ����                                                                                                                                                                                                                                                                                                                            f           g           V        Y'q�     �   e   f           histograms.append(JetHistograms)   $histograms.append(MuonJetHistograms)5�_�                    p        ����                                                                                                                                                                                                                                                                                                                            p           r           V        Y'q�     �   o   p          Dprocess.DisplacedSUSYEventVariableProducer.type = cms.string("data")   H#process.DisplacedSUSYEventVariableProducer.triggerPath = cms.string("")   R#process.DisplacedSUSYEventVariableProducer.triggerScalingFactor = cms.double(1.0)5�_�                    n   u    ����                                                                                                                                                                                                                                                                                                                            p           p           V        Y'r	     �   m   p   o      zadd_channels (process, eventSelections, histograms, weights, scalingfactorproducers, collections, variableProducers, True)5�_�                    o       ����                                                                                                                                                                                                                                                                                                                            q           q           V        Y'r     �   n   p   p      4              collections, variableProducers, False)5�_�                    n   S    ����                                                                                                                                                                                                                                                                                                                            q           q           V        Y'r      �   m   o   p      Tadd_channels (process, eventSelections, histograms, weights, scalingfactorproducers,�   n   o   p    5�_�                     n   T    ����                                                                                                                                                                                                                                                                                                                            q           q           V        Y'r'    �   m   o   p      zadd_channels (process, eventSelections, histograms, weights, scalingfactorproducers,collections, variableProducers, False)5��