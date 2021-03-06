import FWCore.ParameterSet.Config as cms

process = cms.Process("ViewDigi")

# Dump of different types of digis produced 
# by CSC RawToDigi chane

process.load("SimGeneral.MixingModule.mixNoPU_cfi")
process.load("Geometry.MuonCommonData.muonIdealGeometryXML_cfi")
process.load("Geometry.CSCGeometry.cscGeometry_cfi")
process.load("Configuration/StandardSequences/MagneticField_cff")
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.load("Geometry.MuonNumbering.muonNumberingInitialization_cfi")

process.load("Configuration.StandardSequences.RawToDigi_Data_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")



# initialize MessageLogger and output report
process.MessageLogger = cms.Service("MessageLogger",
    #destinations = cms.untracked.vstring('detailedInfo'),
    destinations = cms.untracked.vstring('cout'),
    #destinations = cms.untracked.vstring('DDUStatusDump'),
    debugModules = cms.untracked.vstring('muonCSCDigis'),
    categories = cms.untracked.vstring("CSCDDUEventData|CSCRawToDigi",
    #'CSCDCCUnpacker|CSCRawToDigi', 'StatusDigis', 'StatusDigi', 'CSCRawToDigi', 'CSCDCCUnpacker', 'EventInfo',
    'badData'),
    #DDUStatusDump = cms.untracked.PSet(
    cout = cms.untracked.PSet(
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        #TRACE = cms.untracked.PSet(limit = cms.untracked.int32(0) ),
        noTimeStamps = cms.untracked.bool(False),
        #FwkReport = cms.untracked.PSet(
        #    reportEvery = cms.untracked.int32(1),
        #    limit = cms.untracked.int32(10000000)
        #),
        #CSCRawToDigi = cms.untracked.PSet(limit = cms.untracked.int32(10000000)),
        #StatusDigi = cms.untracked.PSet(limit = cms.untracked.int32(10000000)),
        #EventInfo = cms.untracked.PSet(limit = cms.untracked.int32(10000000)),

        default = cms.untracked.PSet(limit = cms.untracked.int32(10000000)),
        #Root_NoDictionary = cms.untracked.PSet(limit = cms.untracked.int32(0)),
        DEBUG = cms.untracked.PSet(limit = cms.untracked.int32(0)),
        #FwkJob = cms.untracked.PSet(limit = cms.untracked.int32(0)),
        #FwkSummary = cms.untracked.PSet(reportEvery = cms.untracked.int32(1), limit = cms.untracked.int32(10000000) ),
        threshold = cms.untracked.string('DEBUG')
    )
)

#process.GlobalTag.globaltag = 'CRAFT_V3P::All' CRAFT09_R_V10 GR10_P_V5
#process.GlobalTag.globaltag ='GR10_P_V5::All'
#process.GlobalTag.globaltag ='CRAFT09_R_V10::All'
#process.GlobalTag.globaltag ='GR_R_35X_V7::All'
process.GlobalTag.globaltag = 'GR_R_50_V1::All'

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    #debugFlag = cms.untracked.bool(True),
    #skipEvents = cms.untracked.uint32(3912),
    #skipEvents = cms.untracked.uint32(37), # for 440
    #skipEvents = cms.untracked.uint32(719),
    #skipEvents = cms.untracked.uint32(1392),
    #debugVebosity = cms.untracked.uint32(10),
    fileNames = cms.untracked.vstring(
    #'rfio:/castor/cern.ch/cms/store/mc/Spring10/MinBias/GEN-SIM-RAW/START3X_V25B-v1/0101/FEE113B8-5239-DF11-AEF2-0026189438A2.root'
   #'rfio:/tmp/asakharo/FC58EA9C-4D40-DF11-928D-000423D98804.root',
   #'/store/data/Commissioning10/MinimumBias/RAW/v4/000/132/601/FC58EA9C-4D40-DF11-928D-000423D98804.root'
   # 'rfio:/tmp/asakharo/FE5D634A-6ACE-DE11-8CB8-0030487A18F2.root'
   #'/store/data/BeamCommissioning09/Cosmics/RAW/v1/000/120/331/FE5D634A-6ACE-DE11-8CB8-0030487A18F2.root'
   #'rfio:/tmp/asakharo/440.root'  #from 13601 run
   'rfio:/tmp/asakharo/RUN2011B/SingleMu/176848/32F69BAB-5AE4-E011-A3D0-E0CB4E553651.root'
    )
)

process.muonCSCDigis.UnpackStatusDigis=cms.bool(True)
process.muonCSCDigis.SuppressZeroLCT=cms.untracked.bool(True)
# Accounts the right product name 
# in MC
#process.muonCSCDigis.InputObjects = cms.InputTag("rawDataCollector")
# Inspect FEDs in corrupted events
#process.muonCSCDigis.VisualFEDInspect = cms.untracked.bool(True)
# Short format in the Unpacker envent dumper
#process.muonCSCDigis.VisualFEDShort = cms.untracked.bool(True)
# Dump a whole event from the Unpacker event dumper
process.muonCSCDigis.FormatedEventDump = cms.untracked.bool(True)

# Unpack status digi
# process.muonCSCDigis.UnpackStatusDigis = cms.bool(True)


process.load("EventFilter.CSCRawToDigi.veiwDigi_cfi")

process.dumpCSCdigi.WiresDigiDump = cms.untracked.bool(False)
process.dumpCSCdigi.StripDigiDump = cms.untracked.bool(False)
process.dumpCSCdigi.ComparatorDigiDump = cms.untracked.bool(False)
process.dumpCSCdigi.RpcDigiDump = cms.untracked.bool(False)
process.dumpCSCdigi.AlctDigiDump = cms.untracked.bool(False)
process.dumpCSCdigi.ClctDigiDump = cms.untracked.bool(False)
process.dumpCSCdigi.CorrClctDigiDump = cms.untracked.bool(False)
process.dumpCSCdigi.StatusCFEBDump = cms.untracked.bool(False)
process.dumpCSCdigi.StatusDigiDump = cms.untracked.bool(False)
process.dumpCSCdigi.DDUStatus = cms.untracked.bool(False)
process.dumpCSCdigi.DCCStatus = cms.untracked.bool(False)

process.out = cms.OutputModule("PoolOutputModule",
                      dataset = cms.untracked.PSet(dataTier = cms.untracked.string('DIGI')),
                               fileName = cms.untracked.string('digi_test.root'),
                               )

process.EventContent=cms.EDAnalyzer('EventContentAnalyzer')

process.p1 = cms.Path(process.muonCSCDigis)
#process.p2 = cms.Path(process.EventContent)
process.p3 = cms.Path(process.dumpCSCdigi)
#process.p4 = cms.EndPath(process.out)