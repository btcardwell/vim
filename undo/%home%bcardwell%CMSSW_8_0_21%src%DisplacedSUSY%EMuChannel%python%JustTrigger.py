Vim�UnDo� %�`E�̟�U���Tc<��LM.#���؀�                    	          	   	    Y'v�    _�                             ����                                                                                                                                                                                                                                                                                                                                                             Y'vW     �                 (import FWCore.ParameterSet.Config as cms5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Y'vX     �                A### Set up the preselection for the displaced SUSY analysis #####5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Y'va     �                A#################################################################5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Y'vc     �      	          A#################################################################5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        Y'vz     �                G### jet selection (just for plotting purposes, doesn't make event cuts)   %Preselection.cuts.append(jet_eta_cut)   'Preselection.cuts.append(jet_pt_30_cut)   $Preselection.cuts.append(jet_id_cut)   ### at least one good electron   *Preselection.cuts.append(electron_eta_cut)   +Preselection.cuts.append(electron_gap_veto)   ,Preselection.cuts.append(electron_pt_42_cut)   )Preselection.cuts.append(electron_id_cut)   *Preselection.cuts.append(electron_iso_cut)   ### at least one good muon   &Preselection.cuts.append(muon_eta_cut)   (Preselection.cuts.append(muon_pt_40_cut)   )Preselection.cuts.append(muon_global_cut)   %Preselection.cuts.append(muon_id_cut)   &Preselection.cuts.append(muon_iso_cut)        5�_�      	              
        ����                                                                                                                                                                                                                                                                                                                                                  V        Y'v�     �   	             Preselection = cms.PSet(5�_�                  	           ����                                                                                                                                                                                                                                                                                                                                                  V        Y'v�    �   
             &    name = cms.string("Preselection"),5��