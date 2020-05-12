#include "SampleAnalyzer/User/Analyzer/user.h"
using namespace MA5;

bool user::Initialize(const MA5::Configuration& cfg,
                      const std::map<std::string,std::string>& parameters)
{
  // Initializing PhysicsService for MC
  PHYSICS->mcConfig().Reset();

  // definition of the multiparticle "hadronic"
  PHYSICS->mcConfig().AddHadronicId(-5);
  PHYSICS->mcConfig().AddHadronicId(-4);
  PHYSICS->mcConfig().AddHadronicId(-3);
  PHYSICS->mcConfig().AddHadronicId(-2);
  PHYSICS->mcConfig().AddHadronicId(-1);
  PHYSICS->mcConfig().AddHadronicId(1);
  PHYSICS->mcConfig().AddHadronicId(2);
  PHYSICS->mcConfig().AddHadronicId(3);
  PHYSICS->mcConfig().AddHadronicId(4);
  PHYSICS->mcConfig().AddHadronicId(5);
  PHYSICS->mcConfig().AddHadronicId(21);

  // definition of the multiparticle "invisible"
  PHYSICS->mcConfig().AddInvisibleId(-16);
  PHYSICS->mcConfig().AddInvisibleId(-14);
  PHYSICS->mcConfig().AddInvisibleId(-12);
  PHYSICS->mcConfig().AddInvisibleId(12);
  PHYSICS->mcConfig().AddInvisibleId(14);
  PHYSICS->mcConfig().AddInvisibleId(16);
  PHYSICS->mcConfig().AddInvisibleId(1000022);

  // ===== Signal region ===== //
  Manager()->AddRegionSelection("myregion");

  // ===== Selections ===== //

  // ===== Histograms ===== //
  Manager()->AddHisto("1_sdETA", 400,-10.0,10.0);

  // No problem during initialization
  return true;
}

bool user::Execute(SampleFormat& sample, const EventFormat& event)
{
  MAfloat32 __event_weight__ = 1.0;
  if (weighted_events_ && event.mc()!=0) __event_weight__ = event.mc()->weight();

  if (sample.mc()!=0) sample.mc()->addWeightedEvents(__event_weight__);
  Manager()->InitializeForNewEvent(__event_weight__);

  // Clearing particle containers
  {
      _P_jets_I1I_PTorderingfinalstate_REG_.clear();
      _P_jets_I2I_PTorderingfinalstate_REG_.clear();
      _P_jetsPTorderingfinalstate_REG_.clear();
  }

  // Filling particle containers
  {
    for (MAuint32 i=0;i<event.mc()->particles().size();i++)
    {
      if (isP__jetsPTorderingfinalstate((&(event.mc()->particles()[i])))) _P_jetsPTorderingfinalstate_REG_.push_back(&(event.mc()->particles()[i]));
    }
  }

  // Sorting particles
  // Sorting particle collection according to PTordering
  // for getting 1th particle
  _P_jets_I1I_PTorderingfinalstate_REG_=SORTER->rankFilter(_P_jetsPTorderingfinalstate_REG_,1,PTordering);

  // Sorting particle collection according to PTordering
  // for getting 2th particle
  _P_jets_I2I_PTorderingfinalstate_REG_=SORTER->rankFilter(_P_jetsPTorderingfinalstate_REG_,2,PTordering);

  // Histogram number 1
  //   * Plot: sdETA ( jets[1] jets[2] ) 
  {
  {
    MAuint32 ind[2];
    std::vector<std::set<const MCParticleFormat*> > combis;
    for (ind[0]=0;ind[0]<_P_jets_I1I_PTorderingfinalstate_REG_.size();ind[0]++)
    {
    for (ind[1]=0;ind[1]<_P_jets_I2I_PTorderingfinalstate_REG_.size();ind[1]++)
    {
    if (_P_jets_I2I_PTorderingfinalstate_REG_[ind[1]]==_P_jets_I1I_PTorderingfinalstate_REG_[ind[0]]) continue;

    // Checking if consistent combination
    std::set<const MCParticleFormat*> mycombi;
    for (MAuint32 i=0;i<2;i++)
    {
      mycombi.insert(_P_jets_I1I_PTorderingfinalstate_REG_[ind[i]]);
      mycombi.insert(_P_jets_I2I_PTorderingfinalstate_REG_[ind[i]]);
    }
    MAbool matched=false;
    for (MAuint32 i=0;i<combis.size();i++)
      if (combis[i]==mycombi) {matched=true; break;}
    if (matched) continue;
    else combis.push_back(mycombi);

    MAdouble64 value=0;
    value+=_P_jets_I1I_PTorderingfinalstate_REG_[ind[0]]->eta();
    value-=_P_jets_I2I_PTorderingfinalstate_REG_[ind[1]]->eta();
      Manager()->FillHisto("1_sdETA", value);
    }
    }
  }
  }

  return true;
}

void user::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
}
