Vim�UnDo� ��.u&WM�$�So�'�̚��[}�:�������                                     Y'pY    _�                            ����                                                                                                                                                                                                                                                                                                                                                             Y'p-     �               A### Set up the preselection for the displaced SUSY analysis #####5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Y'p0     �               A#################################################################5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Y'p0     �               @################################################################5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Y'p0     �               ?###############################################################5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Y'p0     �               >##############################################################5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Y'p0     �               =#############################################################5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Y'p3     �      	         A#################################################################5�_�      	              
        ����                                                                                                                                                                                                                                                                                                                            
                    V       Y'pE     �   	             Preselection = cms.PSet(5�_�      
           	           ����                                                                                                                                                                                                                                                                                                                            
                    V       Y'pF     �   
             &    name = cms.string("Preselection"),5�_�   	              
           ����                                                                                                                                                                                                                                                                                                                            
                    V       Y'pV     �                G### jet selection (just for plotting purposes, doesn't make event cuts)   %Preselection.cuts.append(jet_eta_cut)   'Preselection.cuts.append(jet_pt_30_cut)   $Preselection.cuts.append(jet_id_cut)   ### at least two good muons   &Preselection.cuts.append(muon_eta_cut)   (Preselection.cuts.append(muon_pt_40_cut)   )Preselection.cuts.append(muon_global_cut)   %Preselection.cuts.append(muon_id_cut)   &Preselection.cuts.append(muon_iso_cut)    5�_�   
                          ����                                                                                                                                                                                                                                                                                                                            
                    V       Y'pX    �                 5��