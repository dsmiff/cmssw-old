import FWCore.ParameterSet.Config as cms

process = cms.Process("GCT020")

## Import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore/MessageService/MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration/StandardSequences/SimL1Emulator_cff')
process.load('Configuration/StandardSequences/EndOfProcess_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_Data_cff')
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")

## Global tags:
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag.globaltag = cms.string('GR_P_V56')

process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",

        fileNames = cms.untracked.vstring('root://xrootd.unl.edu//store/data/Run2015A/Jet/RAW/v1/000/246/960/00000/7E8B3217-3E0A-E511-A104-02163E0144CE.root')

)

process.gctDigis.numberOfGctSamplesToUnpack = cms.uint32(1)
process.simGctDigis.inputLabel = cms.InputTag('gctDigis')
process.simGctDigis.writeInternalData = cms.bool(True)

# Path
process.p = cms.Path(
    process.gctDigis
    *process.simGctDigis
)

process.output = cms.OutputModule(
    "PoolOutputModule",
    outputCommands = cms.untracked.vstring(
        # 'keep *'
        'drop *',
        'keep *_gctDigis_*_*',
        'keep *_simGctDigis_*_*',
        'keep *_simGctDigisRCT_*_*',
        ),
    fileName = cms.untracked.string('GCTDataEmulator.root')
    )

process.output_step = cms.EndPath(process.output)

process.schedule = cms.Schedule(
    process.p,
    process.output_step
    )
