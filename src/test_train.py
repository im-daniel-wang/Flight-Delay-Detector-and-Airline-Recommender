import pytest
import pandas as pd
import sklearn

from src.train import train_model
from src.train import trainTestSplit

columns = ['length', 'MONTH_1', 'MONTH_2', 'MONTH_3', 'MONTH_4', 'MONTH_5', 'MONTH_6', 'MONTH_7', 'MONTH_8', 'MONTH_9', 'MONTH_10', 'MONTH_11', 'MONTH_12', 'DAY_OF_MONTH_1', 'DAY_OF_MONTH_2', 'DAY_OF_MONTH_3', 'DAY_OF_MONTH_4', 'DAY_OF_MONTH_5', 'DAY_OF_MONTH_6', 'DAY_OF_MONTH_7', 'DAY_OF_MONTH_8', 'DAY_OF_MONTH_9', 'DAY_OF_MONTH_10', 'DAY_OF_MONTH_11', 'DAY_OF_MONTH_12', 'DAY_OF_MONTH_13', 'DAY_OF_MONTH_14', 'DAY_OF_MONTH_15', 'DAY_OF_MONTH_16', 'DAY_OF_MONTH_17', 'DAY_OF_MONTH_18', 'DAY_OF_MONTH_19', 'DAY_OF_MONTH_20', 'DAY_OF_MONTH_21', 'DAY_OF_MONTH_22', 'DAY_OF_MONTH_23', 'DAY_OF_MONTH_24', 'DAY_OF_MONTH_25', 'DAY_OF_MONTH_26', 'DAY_OF_MONTH_27', 'DAY_OF_MONTH_28', 'DAY_OF_MONTH_29', 'DAY_OF_MONTH_30', 'DAY_OF_MONTH_31', 'DAY_OF_WEEK_1', 'DAY_OF_WEEK_2', 'DAY_OF_WEEK_3', 'DAY_OF_WEEK_4', 'DAY_OF_WEEK_5', 'DAY_OF_WEEK_6', 'DAY_OF_WEEK_7', 'dep_hour_0', 'dep_hour_01', 'dep_hour_02', 'dep_hour_03', 'dep_hour_04', 'dep_hour_05', 'dep_hour_06', 'dep_hour_07', 'dep_hour_08', 'dep_hour_09', 'dep_hour_10', 'dep_hour_11', 'dep_hour_12', 'dep_hour_13', 'dep_hour_14', 'dep_hour_15', 'dep_hour_16', 'dep_hour_17', 'dep_hour_18', 'dep_hour_19', 'dep_hour_20', 'dep_hour_21', 'dep_hour_22', 'dep_hour_23', 'OP_UNIQUE_CARRIER_9E', 'OP_UNIQUE_CARRIER_AA', 'OP_UNIQUE_CARRIER_AS', 'OP_UNIQUE_CARRIER_B6', 'OP_UNIQUE_CARRIER_DL', 'OP_UNIQUE_CARRIER_EV', 'OP_UNIQUE_CARRIER_F9', 'OP_UNIQUE_CARRIER_G4', 'OP_UNIQUE_CARRIER_HA', 'OP_UNIQUE_CARRIER_MQ', 'OP_UNIQUE_CARRIER_NK', 'OP_UNIQUE_CARRIER_OH', 'OP_UNIQUE_CARRIER_OO', 'OP_UNIQUE_CARRIER_UA', 'OP_UNIQUE_CARRIER_WN', 'OP_UNIQUE_CARRIER_YV', 'OP_UNIQUE_CARRIER_YX', 'ORIGIN_ABE', 'ORIGIN_ABI', 'ORIGIN_ABQ', 'ORIGIN_ABR', 'ORIGIN_ABY', 'ORIGIN_ACK', 'ORIGIN_ACT', 'ORIGIN_ACV', 'ORIGIN_ACY', 'ORIGIN_ADK', 'ORIGIN_ADQ', 'ORIGIN_AEX', 'ORIGIN_AGS', 'ORIGIN_AKN', 'ORIGIN_ALB', 'ORIGIN_ALO', 'ORIGIN_AMA', 'ORIGIN_ANC', 'ORIGIN_APN', 'ORIGIN_ART', 'ORIGIN_ASE', 'ORIGIN_ATL', 'ORIGIN_ATW', 'ORIGIN_ATY', 'ORIGIN_AUS', 'ORIGIN_AVL', 'ORIGIN_AVP', 'ORIGIN_AZA', 'ORIGIN_AZO', 'ORIGIN_BDL', 'ORIGIN_BET', 'ORIGIN_BFF', 'ORIGIN_BFL', 'ORIGIN_BFM', 'ORIGIN_BGM', 'ORIGIN_BGR', 'ORIGIN_BHM', 'ORIGIN_BIL', 'ORIGIN_BIS', 'ORIGIN_BJI', 'ORIGIN_BKG', 'ORIGIN_BLI', 'ORIGIN_BLV', 'ORIGIN_BMI', 'ORIGIN_BNA', 'ORIGIN_BOI', 'ORIGIN_BOS', 'ORIGIN_BPT', 'ORIGIN_BQK', 'ORIGIN_BQN', 'ORIGIN_BRD', 'ORIGIN_BRO', 'ORIGIN_BRW', 'ORIGIN_BTM', 'ORIGIN_BTR', 'ORIGIN_BTV', 'ORIGIN_BUF', 'ORIGIN_BUR', 'ORIGIN_BWI', 'ORIGIN_BZN', 'ORIGIN_CAE', 'ORIGIN_CAK', 'ORIGIN_CDC', 'ORIGIN_CDV', 'ORIGIN_CGI', 'ORIGIN_CHA', 'ORIGIN_CHO', 'ORIGIN_CHS', 'ORIGIN_CID', 'ORIGIN_CIU', 'ORIGIN_CKB', 'ORIGIN_CLE', 'ORIGIN_CLL', 'ORIGIN_CLT', 'ORIGIN_CMH', 'ORIGIN_CMI', 'ORIGIN_CMX', 'ORIGIN_CNY', 'ORIGIN_COD', 'ORIGIN_COS', 'ORIGIN_COU', 'ORIGIN_CPR', 'ORIGIN_CRP', 'ORIGIN_CRW', 'ORIGIN_CSG', 'ORIGIN_CVG', 'ORIGIN_CWA', 'ORIGIN_CYS', 'ORIGIN_DAB', 'ORIGIN_DAL', 'ORIGIN_DAY', 'ORIGIN_DBQ', 'ORIGIN_DCA', 'ORIGIN_DEN', 'ORIGIN_DFW', 'ORIGIN_DHN', 'ORIGIN_DLG', 'ORIGIN_DLH', 'ORIGIN_DRO', 'ORIGIN_DRT', 'ORIGIN_DSM', 'ORIGIN_DTW', 'ORIGIN_DVL', 'ORIGIN_EAR', 'ORIGIN_EAU', 'ORIGIN_ECP', 'ORIGIN_EGE', 'ORIGIN_EKO', 'ORIGIN_ELM', 'ORIGIN_ELP', 'ORIGIN_ERI', 'ORIGIN_ESC', 'ORIGIN_EUG', 'ORIGIN_EVV', 'ORIGIN_EWN', 'ORIGIN_EWR', 'ORIGIN_EYW', 'ORIGIN_FAI', 'ORIGIN_FAR', 'ORIGIN_FAT', 'ORIGIN_FAY', 'ORIGIN_FCA', 'ORIGIN_FLG', 'ORIGIN_FLL', 'ORIGIN_FNT', 'ORIGIN_FSD', 'ORIGIN_FSM', 'ORIGIN_FWA', 'ORIGIN_GCC', 'ORIGIN_GCK', 'ORIGIN_GEG', 'ORIGIN_GFK', 'ORIGIN_GGG', 'ORIGIN_GJT', 'ORIGIN_GNV', 'ORIGIN_GPT', 'ORIGIN_GRB', 'ORIGIN_GRI', 'ORIGIN_GRK', 'ORIGIN_GRR', 'ORIGIN_GSO', 'ORIGIN_GSP', 'ORIGIN_GTF', 'ORIGIN_GTR', 'ORIGIN_GUC', 'ORIGIN_GUM', 'ORIGIN_HDN', 'ORIGIN_HGR', 'ORIGIN_HHH', 'ORIGIN_HIB', 'ORIGIN_HLN', 'ORIGIN_HNL', 'ORIGIN_HOB', 'ORIGIN_HOU', 'ORIGIN_HPN', 'ORIGIN_HRL', 'ORIGIN_HSV', 'ORIGIN_HTS', 'ORIGIN_HVN', 'ORIGIN_HYA', 'ORIGIN_HYS', 'ORIGIN_IAD', 'ORIGIN_IAG', 'ORIGIN_IAH', 'ORIGIN_ICT', 'ORIGIN_IDA', 'ORIGIN_ILM', 'ORIGIN_IMT', 'ORIGIN_IND', 'ORIGIN_INL', 'ORIGIN_ISN', 'ORIGIN_ISP', 'ORIGIN_ITH', 'ORIGIN_ITO', 'ORIGIN_JAC', 'ORIGIN_JAN', 'ORIGIN_JAX', 'ORIGIN_JFK', 'ORIGIN_JLN', 'ORIGIN_JMS', 'ORIGIN_JNU', 'ORIGIN_KOA', 'ORIGIN_KTN', 'ORIGIN_LAN', 'ORIGIN_LAR', 'ORIGIN_LAS', 'ORIGIN_LAW', 'ORIGIN_LAX', 'ORIGIN_LBB', 'ORIGIN_LBE', 'ORIGIN_LBF', 'ORIGIN_LBL', 'ORIGIN_LCH', 'ORIGIN_LCK', 'ORIGIN_LEX', 'ORIGIN_LFT', 'ORIGIN_LGA', 'ORIGIN_LGB', 'ORIGIN_LIH', 'ORIGIN_LIT', 'ORIGIN_LNK', 'ORIGIN_LRD', 'ORIGIN_LSE', 'ORIGIN_LWB', 'ORIGIN_LWS', 'ORIGIN_LYH', 'ORIGIN_MAF', 'ORIGIN_MBS', 'ORIGIN_MCI', 'ORIGIN_MCO', 'ORIGIN_MDT', 'ORIGIN_MDW', 'ORIGIN_MEI', 'ORIGIN_MEM', 'ORIGIN_MFE', 'ORIGIN_MFR', 'ORIGIN_MGM', 'ORIGIN_MHK', 'ORIGIN_MHT', 'ORIGIN_MIA', 'ORIGIN_MKE', 'ORIGIN_MKG', 'ORIGIN_MLB', 'ORIGIN_MLI', 'ORIGIN_MLU', 'ORIGIN_MMH', 'ORIGIN_MOB', 'ORIGIN_MOT', 'ORIGIN_MQT', 'ORIGIN_MRY', 'ORIGIN_MSN', 'ORIGIN_MSO', 'ORIGIN_MSP', 'ORIGIN_MSY', 'ORIGIN_MTJ', 'ORIGIN_MVY', 'ORIGIN_MYR', 'ORIGIN_OAJ', 'ORIGIN_OAK', 'ORIGIN_OGD', 'ORIGIN_OGG', 'ORIGIN_OGS', 'ORIGIN_OKC', 'ORIGIN_OMA', 'ORIGIN_OME', 'ORIGIN_ONT', 'ORIGIN_ORD', 'ORIGIN_ORF', 'ORIGIN_ORH', 'ORIGIN_OTH', 'ORIGIN_OTZ', 'ORIGIN_OWB', 'ORIGIN_PAE', 'ORIGIN_PAH', 'ORIGIN_PBG', 'ORIGIN_PBI', 'ORIGIN_PDX', 'ORIGIN_PGD', 'ORIGIN_PHF', 'ORIGIN_PHL', 'ORIGIN_PHX', 'ORIGIN_PIA', 'ORIGIN_PIB', 'ORIGIN_PIE', 'ORIGIN_PIH', 'ORIGIN_PIR', 'ORIGIN_PIT', 'ORIGIN_PLN', 'ORIGIN_PNS', 'ORIGIN_PPG', 'ORIGIN_PRC', 'ORIGIN_PSC', 'ORIGIN_PSE', 'ORIGIN_PSG', 'ORIGIN_PSP', 'ORIGIN_PUB', 'ORIGIN_PVD', 'ORIGIN_PVU', 'ORIGIN_PWM', 'ORIGIN_RAP', 'ORIGIN_RDD', 'ORIGIN_RDM', 'ORIGIN_RDU', 'ORIGIN_RFD', 'ORIGIN_RHI', 'ORIGIN_RIC', 'ORIGIN_RKS', 'ORIGIN_RNO', 'ORIGIN_ROA', 'ORIGIN_ROC', 'ORIGIN_ROW', 'ORIGIN_RST', 'ORIGIN_RSW', 'ORIGIN_SAF', 'ORIGIN_SAN', 'ORIGIN_SAT', 'ORIGIN_SAV', 'ORIGIN_SBA', 'ORIGIN_SBN', 'ORIGIN_SBP', 'ORIGIN_SCC', 'ORIGIN_SCE', 'ORIGIN_SCK', 'ORIGIN_SDF', 'ORIGIN_SEA', 'ORIGIN_SFB', 'ORIGIN_SFO', 'ORIGIN_SGF', 'ORIGIN_SGU', 'ORIGIN_SHD', 'ORIGIN_SHV', 'ORIGIN_SIT', 'ORIGIN_SJC', 'ORIGIN_SJT', 'ORIGIN_SJU', 'ORIGIN_SLC', 'ORIGIN_SLN', 'ORIGIN_SMF', 'ORIGIN_SMX', 'ORIGIN_SNA', 'ORIGIN_SPI', 'ORIGIN_SPN', 'ORIGIN_SPS', 'ORIGIN_SRQ', 'ORIGIN_STC', 'ORIGIN_STL', 'ORIGIN_STS', 'ORIGIN_STT', 'ORIGIN_STX', 'ORIGIN_SUN', 'ORIGIN_SUX', 'ORIGIN_SWF', 'ORIGIN_SWO', 'ORIGIN_SYR', 'ORIGIN_TLH', 'ORIGIN_TOL', 'ORIGIN_TPA', 'ORIGIN_TRI', 'ORIGIN_TTN', 'ORIGIN_TUL', 'ORIGIN_TUS', 'ORIGIN_TVC', 'ORIGIN_TWF', 'ORIGIN_TXK', 'ORIGIN_TYR', 'ORIGIN_TYS', 'ORIGIN_UIN', 'ORIGIN_USA', 'ORIGIN_VEL', 'ORIGIN_VLD', 'ORIGIN_VPS', 'ORIGIN_WRG', 'ORIGIN_XNA', 'ORIGIN_XWA', 'ORIGIN_YAK', 'ORIGIN_YUM', 'DEST_ABE', 'DEST_ABI', 'DEST_ABQ', 'DEST_ABR', 'DEST_ABY', 'DEST_ACK', 'DEST_ACT', 'DEST_ACV', 'DEST_ACY', 'DEST_ADK', 'DEST_ADQ', 'DEST_AEX', 'DEST_AGS', 'DEST_AKN', 'DEST_ALB', 'DEST_ALO', 'DEST_AMA', 'DEST_ANC', 'DEST_APN', 'DEST_ART', 'DEST_ASE', 'DEST_ATL', 'DEST_ATW', 'DEST_ATY', 'DEST_AUS', 'DEST_AVL', 'DEST_AVP', 'DEST_AZA', 'DEST_AZO', 'DEST_BDL', 'DEST_BET', 'DEST_BFF', 'DEST_BFL', 'DEST_BFM', 'DEST_BGM', 'DEST_BGR', 'DEST_BHM', 'DEST_BIL', 'DEST_BIS', 'DEST_BJI', 'DEST_BKG', 'DEST_BLI', 'DEST_BLV', 'DEST_BMI', 'DEST_BNA', 'DEST_BOI', 'DEST_BOS', 'DEST_BPT', 'DEST_BQK', 'DEST_BQN', 'DEST_BRD', 'DEST_BRO', 'DEST_BRW', 'DEST_BTM', 'DEST_BTR', 'DEST_BTV', 'DEST_BUF', 'DEST_BUR', 'DEST_BWI', 'DEST_BZN', 'DEST_CAE', 'DEST_CAK', 'DEST_CDC', 'DEST_CDV', 'DEST_CGI', 'DEST_CHA', 'DEST_CHO', 'DEST_CHS', 'DEST_CID', 'DEST_CIU', 'DEST_CKB', 'DEST_CLE', 'DEST_CLL', 'DEST_CLT', 'DEST_CMH', 'DEST_CMI', 'DEST_CMX', 'DEST_CNY', 'DEST_COD', 'DEST_COS', 'DEST_COU', 'DEST_CPR', 'DEST_CRP', 'DEST_CRW', 'DEST_CSG', 'DEST_CVG', 'DEST_CWA', 'DEST_CYS', 'DEST_DAB', 'DEST_DAL', 'DEST_DAY', 'DEST_DBQ', 'DEST_DCA', 'DEST_DEN', 'DEST_DFW', 'DEST_DHN', 'DEST_DLG', 'DEST_DLH', 'DEST_DRO', 'DEST_DRT', 'DEST_DSM', 'DEST_DTW', 'DEST_DVL', 'DEST_EAR', 'DEST_EAU', 'DEST_ECP', 'DEST_EGE', 'DEST_EKO', 'DEST_ELM', 'DEST_ELP', 'DEST_ERI', 'DEST_ESC', 'DEST_EUG', 'DEST_EVV', 'DEST_EWN', 'DEST_EWR', 'DEST_EYW', 'DEST_FAI', 'DEST_FAR', 'DEST_FAT', 'DEST_FAY', 'DEST_FCA', 'DEST_FLG', 'DEST_FLL', 'DEST_FNT', 'DEST_FSD', 'DEST_FSM', 'DEST_FWA', 'DEST_GCC', 'DEST_GCK', 'DEST_GEG', 'DEST_GFK', 'DEST_GGG', 'DEST_GJT', 'DEST_GNV', 'DEST_GPT', 'DEST_GRB', 'DEST_GRI', 'DEST_GRK', 'DEST_GRR', 'DEST_GSO', 'DEST_GSP', 'DEST_GST', 'DEST_GTF', 'DEST_GTR', 'DEST_GUC', 'DEST_GUM', 'DEST_HDN', 'DEST_HGR', 'DEST_HHH', 'DEST_HIB', 'DEST_HLN', 'DEST_HNL', 'DEST_HOB', 'DEST_HOU', 'DEST_HPN', 'DEST_HRL', 'DEST_HSV', 'DEST_HTS', 'DEST_HVN', 'DEST_HYA', 'DEST_HYS', 'DEST_IAD', 'DEST_IAG', 'DEST_IAH', 'DEST_ICT', 'DEST_IDA', 'DEST_ILM', 'DEST_IMT', 'DEST_IND', 'DEST_INL', 'DEST_ISN', 'DEST_ISP', 'DEST_ITH', 'DEST_ITO', 'DEST_JAC', 'DEST_JAN', 'DEST_JAX', 'DEST_JFK', 'DEST_JLN', 'DEST_JMS', 'DEST_JNU', 'DEST_KOA', 'DEST_KTN', 'DEST_LAN', 'DEST_LAR', 'DEST_LAS', 'DEST_LAW', 'DEST_LAX', 'DEST_LBB', 'DEST_LBE', 'DEST_LBF', 'DEST_LBL', 'DEST_LCH', 'DEST_LCK', 'DEST_LEX', 'DEST_LFT', 'DEST_LGA', 'DEST_LGB', 'DEST_LIH', 'DEST_LIT', 'DEST_LNK', 'DEST_LRD', 'DEST_LSE', 'DEST_LWB', 'DEST_LWS', 'DEST_LYH', 'DEST_MAF', 'DEST_MBS', 'DEST_MCI', 'DEST_MCO', 'DEST_MDT', 'DEST_MDW', 'DEST_MEI', 'DEST_MEM', 'DEST_MFE', 'DEST_MFR', 'DEST_MGM', 'DEST_MHK', 'DEST_MHT', 'DEST_MIA', 'DEST_MKE', 'DEST_MKG', 'DEST_MLB', 'DEST_MLI', 'DEST_MLU', 'DEST_MMH', 'DEST_MOB', 'DEST_MOT', 'DEST_MQT', 'DEST_MRY', 'DEST_MSN', 'DEST_MSO', 'DEST_MSP', 'DEST_MSY', 'DEST_MTJ', 'DEST_MVY', 'DEST_MYR', 'DEST_OAJ', 'DEST_OAK', 'DEST_OGD', 'DEST_OGG', 'DEST_OGS', 'DEST_OKC', 'DEST_OMA', 'DEST_OME', 'DEST_ONT', 'DEST_ORD', 'DEST_ORF', 'DEST_ORH', 'DEST_OTH', 'DEST_OTZ', 'DEST_OWB', 'DEST_PAE', 'DEST_PAH', 'DEST_PBG', 'DEST_PBI', 'DEST_PDX', 'DEST_PGD', 'DEST_PHF', 'DEST_PHL', 'DEST_PHX', 'DEST_PIA', 'DEST_PIB', 'DEST_PIE', 'DEST_PIH', 'DEST_PIR', 'DEST_PIT', 'DEST_PLN', 'DEST_PNS', 'DEST_PPG', 'DEST_PRC', 'DEST_PSC', 'DEST_PSE', 'DEST_PSG', 'DEST_PSM', 'DEST_PSP', 'DEST_PUB', 'DEST_PVD', 'DEST_PVU', 'DEST_PWM', 'DEST_RAP', 'DEST_RDD', 'DEST_RDM', 'DEST_RDU', 'DEST_RFD', 'DEST_RHI', 'DEST_RIC', 'DEST_RKS', 'DEST_RNO', 'DEST_ROA', 'DEST_ROC', 'DEST_ROW', 'DEST_RST', 'DEST_RSW', 'DEST_SAF', 'DEST_SAN', 'DEST_SAT', 'DEST_SAV', 'DEST_SBA', 'DEST_SBN', 'DEST_SBP', 'DEST_SCC', 'DEST_SCE', 'DEST_SCK', 'DEST_SDF', 'DEST_SEA', 'DEST_SFB', 'DEST_SFO', 'DEST_SGF', 'DEST_SGU', 'DEST_SHD', 'DEST_SHV', 'DEST_SIT', 'DEST_SJC', 'DEST_SJT', 'DEST_SJU', 'DEST_SLC', 'DEST_SLN', 'DEST_SMF', 'DEST_SMX', 'DEST_SNA', 'DEST_SPI', 'DEST_SPN', 'DEST_SPS', 'DEST_SRQ', 'DEST_STL', 'DEST_STS', 'DEST_STT', 'DEST_STX', 'DEST_SUN', 'DEST_SUX', 'DEST_SWF', 'DEST_SWO', 'DEST_SYR', 'DEST_TLH', 'DEST_TOL', 'DEST_TPA', 'DEST_TRI', 'DEST_TTN', 'DEST_TUL', 'DEST_TUS', 'DEST_TVC', 'DEST_TWF', 'DEST_TXK', 'DEST_TYR', 'DEST_TYS', 'DEST_UIN', 'DEST_USA', 'DEST_VEL', 'DEST_VLD', 'DEST_VPS', 'DEST_WRG', 'DEST_WYS', 'DEST_XNA', 'DEST_XWA', 'DEST_YAK', 'DEST_YUM', 'delay']
data = [[6.0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"on_time"],
        [1.0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"delay"],
        [1.0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"on_time"],
]

columns_bad = ['length', 'MONTH_1', 'MONTH_2', 'MONTH_3', 'MONTH_4', 'MONTH_5', 'MONTH_6', 'MONTH_7', 'MONTH_8', 'MONTH_9', 'MONTH_10', 'MONTH_11', 'MONTH_12', 'DAY_OF_MONTH_1', 'DAY_OF_MONTH_2', 'DAY_OF_MONTH_3', 'DAY_OF_MONTH_4', 'DAY_OF_MONTH_5', 'DAY_OF_MONTH_6', 'DAY_OF_MONTH_7', 'DAY_OF_MONTH_8', 'DAY_OF_MONTH_9', 'DAY_OF_MONTH_10', 'DAY_OF_MONTH_11', 'DAY_OF_MONTH_12', 'DAY_OF_MONTH_13', 'DAY_OF_MONTH_14', 'DAY_OF_MONTH_15', 'DAY_OF_MONTH_16', 'DAY_OF_MONTH_17', 'DAY_OF_MONTH_18', 'DAY_OF_MONTH_19', 'DAY_OF_MONTH_20', 'DAY_OF_MONTH_21', 'DAY_OF_MONTH_22', 'DAY_OF_MONTH_23', 'DAY_OF_MONTH_24', 'DAY_OF_MONTH_25', 'DAY_OF_MONTH_26', 'DAY_OF_MONTH_27', 'DAY_OF_MONTH_28', 'DAY_OF_MONTH_29', 'DAY_OF_MONTH_30', 'DAY_OF_MONTH_31', 'DAY_OF_WEEK_1', 'DAY_OF_WEEK_2', 'DAY_OF_WEEK_3', 'DAY_OF_WEEK_4', 'DAY_OF_WEEK_5', 'DAY_OF_WEEK_6', 'DAY_OF_WEEK_7', 'dep_hour_0', 'dep_hour_01', 'dep_hour_02', 'dep_hour_03', 'dep_hour_04', 'dep_hour_05', 'dep_hour_06', 'dep_hour_07', 'dep_hour_08', 'dep_hour_09', 'dep_hour_10', 'dep_hour_11', 'dep_hour_12', 'dep_hour_13', 'dep_hour_14', 'dep_hour_15', 'dep_hour_16', 'dep_hour_17', 'dep_hour_18', 'dep_hour_19', 'dep_hour_20', 'dep_hour_21', 'dep_hour_22', 'dep_hour_23', 'OP_UNIQUE_CARRIER_9E', 'OP_UNIQUE_CARRIER_AA', 'OP_UNIQUE_CARRIER_AS', 'OP_UNIQUE_CARRIER_B6', 'OP_UNIQUE_CARRIER_DL', 'OP_UNIQUE_CARRIER_EV', 'OP_UNIQUE_CARRIER_F9', 'OP_UNIQUE_CARRIER_G4', 'OP_UNIQUE_CARRIER_HA', 'OP_UNIQUE_CARRIER_MQ', 'OP_UNIQUE_CARRIER_NK', 'OP_UNIQUE_CARRIER_OH', 'OP_UNIQUE_CARRIER_OO', 'OP_UNIQUE_CARRIER_UA', 'OP_UNIQUE_CARRIER_WN', 'OP_UNIQUE_CARRIER_YV', 'OP_UNIQUE_CARRIER_YX', 'ORIGIN_ABE', 'ORIGIN_ABI', 'ORIGIN_ABQ', 'ORIGIN_ABR', 'ORIGIN_ABY', 'ORIGIN_ACK', 'ORIGIN_ACT', 'ORIGIN_ACV', 'ORIGIN_ACY', 'ORIGIN_ADK', 'ORIGIN_ADQ', 'ORIGIN_AEX', 'ORIGIN_AGS', 'ORIGIN_AKN', 'ORIGIN_ALB', 'ORIGIN_ALO', 'ORIGIN_AMA', 'ORIGIN_ANC', 'ORIGIN_APN', 'ORIGIN_ART', 'ORIGIN_ASE', 'ORIGIN_ATL', 'ORIGIN_ATW', 'ORIGIN_ATY', 'ORIGIN_AUS', 'ORIGIN_AVL', 'ORIGIN_AVP', 'ORIGIN_AZA', 'ORIGIN_AZO', 'ORIGIN_BDL', 'ORIGIN_BET', 'ORIGIN_BFF', 'ORIGIN_BFL', 'ORIGIN_BFM', 'ORIGIN_BGM', 'ORIGIN_BGR', 'ORIGIN_BHM', 'ORIGIN_BIL', 'ORIGIN_BIS', 'ORIGIN_BJI', 'ORIGIN_BKG', 'ORIGIN_BLI', 'ORIGIN_BLV', 'ORIGIN_BMI', 'ORIGIN_BNA', 'ORIGIN_BOI', 'ORIGIN_BOS', 'ORIGIN_BPT', 'ORIGIN_BQK', 'ORIGIN_BQN', 'ORIGIN_BRD', 'ORIGIN_BRO', 'ORIGIN_BRW', 'ORIGIN_BTM', 'ORIGIN_BTR', 'ORIGIN_BTV', 'ORIGIN_BUF', 'ORIGIN_BUR', 'ORIGIN_BWI', 'ORIGIN_BZN', 'ORIGIN_CAE', 'ORIGIN_CAK', 'ORIGIN_CDC', 'ORIGIN_CDV', 'ORIGIN_CGI', 'ORIGIN_CHA', 'ORIGIN_CHO', 'ORIGIN_CHS', 'ORIGIN_CID', 'ORIGIN_CIU', 'ORIGIN_CKB', 'ORIGIN_CLE', 'ORIGIN_CLL', 'ORIGIN_CLT', 'ORIGIN_CMH', 'ORIGIN_CMI', 'ORIGIN_CMX', 'ORIGIN_CNY', 'ORIGIN_COD', 'ORIGIN_COS', 'ORIGIN_COU', 'ORIGIN_CPR', 'ORIGIN_CRP', 'ORIGIN_CRW', 'ORIGIN_CSG', 'ORIGIN_CVG', 'ORIGIN_CWA', 'ORIGIN_CYS', 'ORIGIN_DAB', 'ORIGIN_DAL', 'ORIGIN_DAY', 'ORIGIN_DBQ', 'ORIGIN_DCA', 'ORIGIN_DEN', 'ORIGIN_DFW', 'ORIGIN_DHN', 'ORIGIN_DLG', 'ORIGIN_DLH', 'ORIGIN_DRO', 'ORIGIN_DRT', 'ORIGIN_DSM', 'ORIGIN_DTW', 'ORIGIN_DVL', 'ORIGIN_EAR', 'ORIGIN_EAU', 'ORIGIN_ECP', 'ORIGIN_EGE', 'ORIGIN_EKO', 'ORIGIN_ELM', 'ORIGIN_ELP', 'ORIGIN_ERI', 'ORIGIN_ESC', 'ORIGIN_EUG', 'ORIGIN_EVV', 'ORIGIN_EWN', 'ORIGIN_EWR', 'ORIGIN_EYW', 'ORIGIN_FAI', 'ORIGIN_FAR', 'ORIGIN_FAT', 'ORIGIN_FAY', 'ORIGIN_FCA', 'ORIGIN_FLG', 'ORIGIN_FLL', 'ORIGIN_FNT', 'ORIGIN_FSD', 'ORIGIN_FSM', 'ORIGIN_FWA', 'ORIGIN_GCC', 'ORIGIN_GCK', 'ORIGIN_GEG', 'ORIGIN_GFK', 'ORIGIN_GGG', 'ORIGIN_GJT', 'ORIGIN_GNV', 'ORIGIN_GPT', 'ORIGIN_GRB', 'ORIGIN_GRI', 'ORIGIN_GRK', 'ORIGIN_GRR', 'ORIGIN_GSO', 'ORIGIN_GSP', 'ORIGIN_GTF', 'ORIGIN_GTR', 'ORIGIN_GUC', 'ORIGIN_GUM', 'ORIGIN_HDN', 'ORIGIN_HGR', 'ORIGIN_HHH', 'ORIGIN_HIB', 'ORIGIN_HLN', 'ORIGIN_HNL', 'ORIGIN_HOB', 'ORIGIN_HOU', 'ORIGIN_HPN', 'ORIGIN_HRL', 'ORIGIN_HSV', 'ORIGIN_HTS', 'ORIGIN_HVN', 'ORIGIN_HYA', 'ORIGIN_HYS', 'ORIGIN_IAD', 'ORIGIN_IAG', 'ORIGIN_IAH', 'ORIGIN_ICT', 'ORIGIN_IDA', 'ORIGIN_ILM', 'ORIGIN_IMT', 'ORIGIN_IND', 'ORIGIN_INL', 'ORIGIN_ISN', 'ORIGIN_ISP', 'ORIGIN_ITH', 'ORIGIN_ITO', 'ORIGIN_JAC', 'ORIGIN_JAN', 'ORIGIN_JAX', 'ORIGIN_JFK', 'ORIGIN_JLN', 'ORIGIN_JMS', 'ORIGIN_JNU', 'ORIGIN_KOA', 'ORIGIN_KTN', 'ORIGIN_LAN', 'ORIGIN_LAR', 'ORIGIN_LAS', 'ORIGIN_LAW', 'ORIGIN_LAX', 'ORIGIN_LBB', 'ORIGIN_LBE', 'ORIGIN_LBF', 'ORIGIN_LBL', 'ORIGIN_LCH', 'ORIGIN_LCK', 'ORIGIN_LEX', 'ORIGIN_LFT', 'ORIGIN_LGA', 'ORIGIN_LGB', 'ORIGIN_LIH', 'ORIGIN_LIT', 'ORIGIN_LNK', 'ORIGIN_LRD', 'ORIGIN_LSE', 'ORIGIN_LWB', 'ORIGIN_LWS', 'ORIGIN_LYH', 'ORIGIN_MAF', 'ORIGIN_MBS', 'ORIGIN_MCI', 'ORIGIN_MCO', 'ORIGIN_MDT', 'ORIGIN_MDW', 'ORIGIN_MEI', 'ORIGIN_MEM', 'ORIGIN_MFE', 'ORIGIN_MFR', 'ORIGIN_MGM', 'ORIGIN_MHK', 'ORIGIN_MHT', 'ORIGIN_MIA', 'ORIGIN_MKE', 'ORIGIN_MKG', 'ORIGIN_MLB', 'ORIGIN_MLI', 'ORIGIN_MLU', 'ORIGIN_MMH', 'ORIGIN_MOB', 'ORIGIN_MOT', 'ORIGIN_MQT', 'ORIGIN_MRY', 'ORIGIN_MSN', 'ORIGIN_MSO', 'ORIGIN_MSP', 'ORIGIN_MSY', 'ORIGIN_MTJ', 'ORIGIN_MVY', 'ORIGIN_MYR', 'ORIGIN_OAJ', 'ORIGIN_OAK', 'ORIGIN_OGD', 'ORIGIN_OGG', 'ORIGIN_OGS', 'ORIGIN_OKC', 'ORIGIN_OMA', 'ORIGIN_OME', 'ORIGIN_ONT', 'ORIGIN_ORD', 'ORIGIN_ORF', 'ORIGIN_ORH', 'ORIGIN_OTH', 'ORIGIN_OTZ', 'ORIGIN_OWB', 'ORIGIN_PAE', 'ORIGIN_PAH', 'ORIGIN_PBG', 'ORIGIN_PBI', 'ORIGIN_PDX', 'ORIGIN_PGD', 'ORIGIN_PHF', 'ORIGIN_PHL', 'ORIGIN_PHX', 'ORIGIN_PIA', 'ORIGIN_PIB', 'ORIGIN_PIE', 'ORIGIN_PIH', 'ORIGIN_PIR', 'ORIGIN_PIT', 'ORIGIN_PLN', 'ORIGIN_PNS', 'ORIGIN_PPG', 'ORIGIN_PRC', 'ORIGIN_PSC', 'ORIGIN_PSE', 'ORIGIN_PSG', 'ORIGIN_PSP', 'ORIGIN_PUB', 'ORIGIN_PVD', 'ORIGIN_PVU', 'ORIGIN_PWM', 'ORIGIN_RAP', 'ORIGIN_RDD', 'ORIGIN_RDM', 'ORIGIN_RDU', 'ORIGIN_RFD', 'ORIGIN_RHI', 'ORIGIN_RIC', 'ORIGIN_RKS', 'ORIGIN_RNO', 'ORIGIN_ROA', 'ORIGIN_ROC', 'ORIGIN_ROW', 'ORIGIN_RST', 'ORIGIN_RSW', 'ORIGIN_SAF', 'ORIGIN_SAN', 'ORIGIN_SAT', 'ORIGIN_SAV', 'ORIGIN_SBA', 'ORIGIN_SBN', 'ORIGIN_SBP', 'ORIGIN_SCC', 'ORIGIN_SCE', 'ORIGIN_SCK', 'ORIGIN_SDF', 'ORIGIN_SEA', 'ORIGIN_SFB', 'ORIGIN_SFO', 'ORIGIN_SGF', 'ORIGIN_SGU', 'ORIGIN_SHD', 'ORIGIN_SHV', 'ORIGIN_SIT', 'ORIGIN_SJC', 'ORIGIN_SJT', 'ORIGIN_SJU', 'ORIGIN_SLC', 'ORIGIN_SLN', 'ORIGIN_SMF', 'ORIGIN_SMX', 'ORIGIN_SNA', 'ORIGIN_SPI', 'ORIGIN_SPN', 'ORIGIN_SPS', 'ORIGIN_SRQ', 'ORIGIN_STC', 'ORIGIN_STL', 'ORIGIN_STS', 'ORIGIN_STT', 'ORIGIN_STX', 'ORIGIN_SUN', 'ORIGIN_SUX', 'ORIGIN_SWF', 'ORIGIN_SWO', 'ORIGIN_SYR', 'ORIGIN_TLH', 'ORIGIN_TOL', 'ORIGIN_TPA', 'ORIGIN_TRI', 'ORIGIN_TTN', 'ORIGIN_TUL', 'ORIGIN_TUS', 'ORIGIN_TVC', 'ORIGIN_TWF', 'ORIGIN_TXK', 'ORIGIN_TYR', 'ORIGIN_TYS', 'ORIGIN_UIN', 'ORIGIN_USA', 'ORIGIN_VEL', 'ORIGIN_VLD', 'ORIGIN_VPS', 'ORIGIN_WRG', 'ORIGIN_XNA', 'ORIGIN_XWA', 'ORIGIN_YAK', 'ORIGIN_YUM', 'DEST_ABE', 'DEST_ABI', 'DEST_ABQ', 'DEST_ABR', 'DEST_ABY', 'DEST_ACK', 'DEST_ACT', 'DEST_ACV', 'DEST_ACY', 'DEST_ADK', 'DEST_ADQ', 'DEST_AEX', 'DEST_AGS', 'DEST_AKN', 'DEST_ALB', 'DEST_ALO', 'DEST_AMA', 'DEST_ANC', 'DEST_APN', 'DEST_ART', 'DEST_ASE', 'DEST_ATL', 'DEST_ATW', 'DEST_ATY', 'DEST_AUS', 'DEST_AVL', 'DEST_AVP', 'DEST_AZA', 'DEST_AZO', 'DEST_BDL', 'DEST_BET', 'DEST_BFF', 'DEST_BFL', 'DEST_BFM', 'DEST_BGM', 'DEST_BGR', 'DEST_BHM', 'DEST_BIL', 'DEST_BIS', 'DEST_BJI', 'DEST_BKG', 'DEST_BLI', 'DEST_BLV', 'DEST_BMI', 'DEST_BNA', 'DEST_BOI', 'DEST_BOS', 'DEST_BPT', 'DEST_BQK', 'DEST_BQN', 'DEST_BRD', 'DEST_BRO', 'DEST_BRW', 'DEST_BTM', 'DEST_BTR', 'DEST_BTV', 'DEST_BUF', 'DEST_BUR', 'DEST_BWI', 'DEST_BZN', 'DEST_CAE', 'DEST_CAK', 'DEST_CDC', 'DEST_CDV', 'DEST_CGI', 'DEST_CHA', 'DEST_CHO', 'DEST_CHS', 'DEST_CID', 'DEST_CIU', 'DEST_CKB', 'DEST_CLE', 'DEST_CLL', 'DEST_CLT', 'DEST_CMH', 'DEST_CMI', 'DEST_CMX', 'DEST_CNY', 'DEST_COD', 'DEST_COS', 'DEST_COU', 'DEST_CPR', 'DEST_CRP', 'DEST_CRW', 'DEST_CSG', 'DEST_CVG', 'DEST_CWA', 'DEST_CYS', 'DEST_DAB', 'DEST_DAL', 'DEST_DAY', 'DEST_DBQ', 'DEST_DCA', 'DEST_DEN', 'DEST_DFW', 'DEST_DHN', 'DEST_DLG', 'DEST_DLH', 'DEST_DRO', 'DEST_DRT', 'DEST_DSM', 'DEST_DTW', 'DEST_DVL', 'DEST_EAR', 'DEST_EAU', 'DEST_ECP', 'DEST_EGE', 'DEST_EKO', 'DEST_ELM', 'DEST_ELP', 'DEST_ERI', 'DEST_ESC', 'DEST_EUG', 'DEST_EVV', 'DEST_EWN', 'DEST_EWR', 'DEST_EYW', 'DEST_FAI', 'DEST_FAR', 'DEST_FAT', 'DEST_FAY', 'DEST_FCA', 'DEST_FLG', 'DEST_FLL', 'DEST_FNT', 'DEST_FSD', 'DEST_FSM', 'DEST_FWA', 'DEST_GCC', 'DEST_GCK', 'DEST_GEG', 'DEST_GFK', 'DEST_GGG', 'DEST_GJT', 'DEST_GNV', 'DEST_GPT', 'DEST_GRB', 'DEST_GRI', 'DEST_GRK', 'DEST_GRR', 'DEST_GSO', 'DEST_GSP', 'DEST_GST', 'DEST_GTF', 'DEST_GTR', 'DEST_GUC', 'DEST_GUM', 'DEST_HDN', 'DEST_HGR', 'DEST_HHH', 'DEST_HIB', 'DEST_HLN', 'DEST_HNL', 'DEST_HOB', 'DEST_HOU', 'DEST_HPN', 'DEST_HRL', 'DEST_HSV', 'DEST_HTS', 'DEST_HVN', 'DEST_HYA', 'DEST_HYS', 'DEST_IAD', 'DEST_IAG', 'DEST_IAH', 'DEST_ICT', 'DEST_IDA', 'DEST_ILM', 'DEST_IMT', 'DEST_IND', 'DEST_INL', 'DEST_ISN', 'DEST_ISP', 'DEST_ITH', 'DEST_ITO', 'DEST_JAC', 'DEST_JAN', 'DEST_JAX', 'DEST_JFK', 'DEST_JLN', 'DEST_JMS', 'DEST_JNU', 'DEST_KOA', 'DEST_KTN', 'DEST_LAN', 'DEST_LAR', 'DEST_LAS', 'DEST_LAW', 'DEST_LAX', 'DEST_LBB', 'DEST_LBE', 'DEST_LBF', 'DEST_LBL', 'DEST_LCH', 'DEST_LCK', 'DEST_LEX', 'DEST_LFT', 'DEST_LGA', 'DEST_LGB', 'DEST_LIH', 'DEST_LIT', 'DEST_LNK', 'DEST_LRD', 'DEST_LSE', 'DEST_LWB', 'DEST_LWS', 'DEST_LYH', 'DEST_MAF', 'DEST_MBS', 'DEST_MCI', 'DEST_MCO', 'DEST_MDT', 'DEST_MDW', 'DEST_MEI', 'DEST_MEM', 'DEST_MFE', 'DEST_MFR', 'DEST_MGM', 'DEST_MHK', 'DEST_MHT', 'DEST_MIA', 'DEST_MKE', 'DEST_MKG', 'DEST_MLB', 'DEST_MLI', 'DEST_MLU', 'DEST_MMH', 'DEST_MOB', 'DEST_MOT', 'DEST_MQT', 'DEST_MRY', 'DEST_MSN', 'DEST_MSO', 'DEST_MSP', 'DEST_MSY', 'DEST_MTJ', 'DEST_MVY', 'DEST_MYR', 'DEST_OAJ', 'DEST_OAK', 'DEST_OGD', 'DEST_OGG', 'DEST_OGS', 'DEST_OKC', 'DEST_OMA', 'DEST_OME', 'DEST_ONT', 'DEST_ORD', 'DEST_ORF', 'DEST_ORH', 'DEST_OTH', 'DEST_OTZ', 'DEST_OWB', 'DEST_PAE', 'DEST_PAH', 'DEST_PBG', 'DEST_PBI', 'DEST_PDX', 'DEST_PGD', 'DEST_PHF', 'DEST_PHL', 'DEST_PHX', 'DEST_PIA', 'DEST_PIB', 'DEST_PIE', 'DEST_PIH', 'DEST_PIR', 'DEST_PIT', 'DEST_PLN', 'DEST_PNS', 'DEST_PPG', 'DEST_PRC', 'DEST_PSC', 'DEST_PSE', 'DEST_PSG', 'DEST_PSM', 'DEST_PSP', 'DEST_PUB', 'DEST_PVD', 'DEST_PVU', 'DEST_PWM', 'DEST_RAP', 'DEST_RDD', 'DEST_RDM', 'DEST_RDU', 'DEST_RFD', 'DEST_RHI', 'DEST_RIC', 'DEST_RKS', 'DEST_RNO', 'DEST_ROA', 'DEST_ROC', 'DEST_ROW', 'DEST_RST', 'DEST_RSW', 'DEST_SAF', 'DEST_SAN', 'DEST_SAT', 'DEST_SAV', 'DEST_SBA', 'DEST_SBN', 'DEST_SBP', 'DEST_SCC', 'DEST_SCE', 'DEST_SCK', 'DEST_SDF', 'DEST_SEA', 'DEST_SFB', 'DEST_SFO', 'DEST_SGF', 'DEST_SGU', 'DEST_SHD', 'DEST_SHV', 'DEST_SIT', 'DEST_SJC', 'DEST_SJT', 'DEST_SJU', 'DEST_SLC', 'DEST_SLN', 'DEST_SMF', 'DEST_SMX', 'DEST_SNA', 'DEST_SPI', 'DEST_SPN', 'DEST_SPS', 'DEST_SRQ', 'DEST_STL', 'DEST_STS', 'DEST_STT', 'DEST_STX', 'DEST_SUN', 'DEST_SUX', 'DEST_SWF', 'DEST_SWO', 'DEST_SYR', 'DEST_TLH', 'DEST_TOL', 'DEST_TPA', 'DEST_TRI', 'DEST_TTN', 'DEST_TUL', 'DEST_TUS', 'DEST_TVC', 'DEST_TWF', 'DEST_TXK', 'DEST_TYR', 'DEST_TYS', 'DEST_UIN', 'DEST_USA', 'DEST_VEL', 'DEST_VLD', 'DEST_VPS', 'DEST_WRG', 'DEST_WYS', 'DEST_XNA', 'DEST_XWA', 'DEST_YAK', 'DEST_YUM']
data_bad = [[6.0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1.0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1.0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]

def test_train_model():
    df = pd.DataFrame(data, columns=columns)
    model = train_model(df, 0.3, "delay", 10)
    assert isinstance(model, sklearn.tree.DecisionTreeClassifier)

def test_train_model_unhappy():
    df = pd.DataFrame(data_bad, columns=columns_bad)
    assert train_model(df, 0.3, "delay", 10) is None



