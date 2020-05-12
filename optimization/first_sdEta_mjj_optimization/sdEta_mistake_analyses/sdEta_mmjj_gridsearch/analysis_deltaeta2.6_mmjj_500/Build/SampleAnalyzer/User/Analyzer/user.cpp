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
  Manager()->AddCut("1_M ( jets[1] jets[2] ) > 120.0");
  Manager()->AddCut("2_sdETA ( jets[1] jets[2] ) > 2.6 and M ( jets[1] jets[2] ) > 500.0");

  // ===== Histograms ===== //
  Manager()->AddHisto("1_PT", 200,0.0,1000.0);
  Manager()->AddHisto("2_ETA", 160,-8.0,8.0);
  Manager()->AddHisto("3_PHI", 64,-3.2,3.2);
  Manager()->AddHisto("4_PT", 100,0.0,500.0);
  Manager()->AddHisto("5_ETA", 160,-8.0,8.0);
  Manager()->AddHisto("6_PHI", 64,-3.2,3.2);
  Manager()->AddHisto("7_DELTAR", 75,0.0,15.0);
  Manager()->AddHisto("8_M", 160,0.0,8000.0);
  Manager()->AddHisto("9_MET", 100,0.0,1000.0);
  Manager()->AddHisto("10_sdETA", 100,-8.0,8.0);
  Manager()->AddHisto("11_M", 400,0.0,1000.0);
  Manager()->AddHisto("12_PT", 80,0.0,1000.0);
  Manager()->AddHisto("13_PT", 400,0.0,1000.0);
  Manager()->AddHisto("14_THT", 80,0.0,1000.0);
  Manager()->AddHisto("15_MET", 200,0.0,1000.0);
  Manager()->AddHisto("16_TET", 80,0.0,1000.0);

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
      _P_a_I1I_PTorderingfinalstate_REG_.clear();
      _P_a_I2I_PTorderingfinalstate_REG_.clear();
      _P_jets_I1I_PTorderingfinalstate_REG_.clear();
      _P_jets_I2I_PTorderingfinalstate_REG_.clear();
      _P_aPTorderingfinalstate_REG_.clear();
      _P_jetsPTorderingfinalstate_REG_.clear();
  }

  // Filling particle containers
  {
    for (MAuint32 i=0;i<event.mc()->particles().size();i++)
    {
      if (isP__aPTorderingfinalstate((&(event.mc()->particles()[i])))) _P_aPTorderingfinalstate_REG_.push_back(&(event.mc()->particles()[i]));
      if (isP__jetsPTorderingfinalstate((&(event.mc()->particles()[i])))) _P_jetsPTorderingfinalstate_REG_.push_back(&(event.mc()->particles()[i]));
    }
  }

  // Sorting particles
  // Sorting particle collection according to PTordering
  // for getting 1th particle
  _P_a_I1I_PTorderingfinalstate_REG_=SORTER->rankFilter(_P_aPTorderingfinalstate_REG_,1,PTordering);

  // Sorting particle collection according to PTordering
  // for getting 2th particle
  _P_a_I2I_PTorderingfinalstate_REG_=SORTER->rankFilter(_P_aPTorderingfinalstate_REG_,2,PTordering);

  // Sorting particle collection according to PTordering
  // for getting 1th particle
  _P_jets_I1I_PTorderingfinalstate_REG_=SORTER->rankFilter(_P_jetsPTorderingfinalstate_REG_,1,PTordering);

  // Sorting particle collection according to PTordering
  // for getting 2th particle
  _P_jets_I2I_PTorderingfinalstate_REG_=SORTER->rankFilter(_P_jetsPTorderingfinalstate_REG_,2,PTordering);

  // Event selection number 1
  //   * Cut: select M ( jets[1] jets[2] ) > 120.0, regions = []
  {
    std::vector<MAbool> filter(1,false);
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

        ParticleBaseFormat q;
        q+=_P_jets_I1I_PTorderingfinalstate_REG_[ind[0]]->momentum();
        q+=_P_jets_I2I_PTorderingfinalstate_REG_[ind[1]]->momentum();
        if (q.m()>120.0) {filter[0]=true; break;}
      }
      }
    }
    }
    MAbool filter_global = (filter[0]);
    if(!Manager()->ApplyCut(filter_global, "1_M ( jets[1] jets[2] ) > 120.0")) return true;
  }

  // Histogram number 1
  //   * Plot: PT ( jets[1] ) 
  {
  {
    MAuint32 ind[1];
    for (ind[0]=0;ind[0]<_P_jets_I1I_PTorderingfinalstate_REG_.size();ind[0]++)
    {
      Manager()->FillHisto("1_PT", _P_jets_I1I_PTorderingfinalstate_REG_[ind[0]]->pt());
    }
  }
  }

  // Histogram number 2
  //   * Plot: ETA ( jets[1] ) 
  {
  {
    MAuint32 ind[1];
    for (ind[0]=0;ind[0]<_P_jets_I1I_PTorderingfinalstate_REG_.size();ind[0]++)
    {
      Manager()->FillHisto("2_ETA", _P_jets_I1I_PTorderingfinalstate_REG_[ind[0]]->eta());
    }
  }
  }

  // Histogram number 3
  //   * Plot: PHI ( jets[1] ) 
  {
  {
    MAuint32 ind[1];
    for (ind[0]=0;ind[0]<_P_jets_I1I_PTorderingfinalstate_REG_.size();ind[0]++)
    {
      Manager()->FillHisto("3_PHI", _P_jets_I1I_PTorderingfinalstate_REG_[ind[0]]->phi());
    }
  }
  }

  // Histogram number 4
  //   * Plot: PT ( jets[2] ) 
  {
  {
    MAuint32 ind[1];
    for (ind[0]=0;ind[0]<_P_jets_I2I_PTorderingfinalstate_REG_.size();ind[0]++)
    {
      Manager()->FillHisto("4_PT", _P_jets_I2I_PTorderingfinalstate_REG_[ind[0]]->pt());
    }
  }
  }

  // Histogram number 5
  //   * Plot: ETA ( jets[2] ) 
  {
  {
    MAuint32 ind[1];
    for (ind[0]=0;ind[0]<_P_jets_I2I_PTorderingfinalstate_REG_.size();ind[0]++)
    {
      Manager()->FillHisto("5_ETA", _P_jets_I2I_PTorderingfinalstate_REG_[ind[0]]->eta());
    }
  }
  }

  // Histogram number 6
  //   * Plot: PHI ( jets[2] ) 
  {
  {
    MAuint32 ind[1];
    for (ind[0]=0;ind[0]<_P_jets_I2I_PTorderingfinalstate_REG_.size();ind[0]++)
    {
      Manager()->FillHisto("6_PHI", _P_jets_I2I_PTorderingfinalstate_REG_[ind[0]]->phi());
    }
  }
  }

  // Histogram number 7
  //   * Plot: DELTAR ( jets[1] , jets[2] ) 
  {
  {
    MAuint32 a[1];
    for (a[0]=0;a[0]<_P_jets_I1I_PTorderingfinalstate_REG_.size();a[0]++)
    {
    MAuint32 b[1];
    for (b[0]=0;b[0]<_P_jets_I2I_PTorderingfinalstate_REG_.size();b[0]++)
    {
     if ( _P_jets_I1I_PTorderingfinalstate_REG_[a[0]] == _P_jets_I2I_PTorderingfinalstate_REG_[b[0]] ) continue;
      Manager()->FillHisto("7_DELTAR", _P_jets_I1I_PTorderingfinalstate_REG_[a[0]]->dr(_P_jets_I2I_PTorderingfinalstate_REG_[b[0]]));
    }
    }
  }
  }

  // Histogram number 8
  //   * Plot: M ( jets[1] jets[2] ) 
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

    ParticleBaseFormat q;
    q+=_P_jets_I1I_PTorderingfinalstate_REG_[ind[0]]->momentum();
    q+=_P_jets_I2I_PTorderingfinalstate_REG_[ind[1]]->momentum();
      Manager()->FillHisto("8_M", q.m());
    }
    }
  }
  }

  // Histogram number 9
  //   * Plot: MET
  {
    Manager()->FillHisto("9_MET", PHYSICS->Transverse->EventMET(event.mc()));
  }

  // Histogram number 10
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
      Manager()->FillHisto("10_sdETA", value);
    }
    }
  }
  }

  // Histogram number 11
  //   * Plot: M ( a[1] a[2] ) 
  {
  {
    MAuint32 ind[2];
    std::vector<std::set<const MCParticleFormat*> > combis;
    for (ind[0]=0;ind[0]<_P_a_I1I_PTorderingfinalstate_REG_.size();ind[0]++)
    {
    for (ind[1]=0;ind[1]<_P_a_I2I_PTorderingfinalstate_REG_.size();ind[1]++)
    {
    if (_P_a_I2I_PTorderingfinalstate_REG_[ind[1]]==_P_a_I1I_PTorderingfinalstate_REG_[ind[0]]) continue;

    // Checking if consistent combination
    std::set<const MCParticleFormat*> mycombi;
    for (MAuint32 i=0;i<2;i++)
    {
      mycombi.insert(_P_a_I1I_PTorderingfinalstate_REG_[ind[i]]);
      mycombi.insert(_P_a_I2I_PTorderingfinalstate_REG_[ind[i]]);
    }
    MAbool matched=false;
    for (MAuint32 i=0;i<combis.size();i++)
      if (combis[i]==mycombi) {matched=true; break;}
    if (matched) continue;
    else combis.push_back(mycombi);

    ParticleBaseFormat q;
    q+=_P_a_I1I_PTorderingfinalstate_REG_[ind[0]]->momentum();
    q+=_P_a_I2I_PTorderingfinalstate_REG_[ind[1]]->momentum();
      Manager()->FillHisto("11_M", q.m());
    }
    }
  }
  }

  // Histogram number 12
  //   * Plot: PT ( a[1] ) 
  {
  {
    MAuint32 ind[1];
    for (ind[0]=0;ind[0]<_P_a_I1I_PTorderingfinalstate_REG_.size();ind[0]++)
    {
      Manager()->FillHisto("12_PT", _P_a_I1I_PTorderingfinalstate_REG_[ind[0]]->pt());
    }
  }
  }

  // Histogram number 13
  //   * Plot: PT ( a[2] ) 
  {
  {
    MAuint32 ind[1];
    for (ind[0]=0;ind[0]<_P_a_I2I_PTorderingfinalstate_REG_.size();ind[0]++)
    {
      Manager()->FillHisto("13_PT", _P_a_I2I_PTorderingfinalstate_REG_[ind[0]]->pt());
    }
  }
  }

  // Histogram number 14
  //   * Plot: THT
  {
    Manager()->FillHisto("14_THT", PHYSICS->Transverse->EventTHT(event.mc()));
  }

  // Histogram number 15
  //   * Plot: MET
  {
    Manager()->FillHisto("15_MET", PHYSICS->Transverse->EventMET(event.mc()));
  }

  // Histogram number 16
  //   * Plot: TET
  {
    Manager()->FillHisto("16_TET", PHYSICS->Transverse->EventTET(event.mc()));
  }

  // Event selection number 2
  //   * Cut: select sdETA ( jets[1] jets[2] ) > 2.6 and M ( jets[1] jets[2] ) > 500.0, regions = []
  {
    std::vector<MAbool> filter(2,false);
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

         if ((_P_jets_I1I_PTorderingfinalstate_REG_[ind[0]]->eta()-_P_jets_I2I_PTorderingfinalstate_REG_[ind[1]]->eta())>2.6) {filter[0]=true; break;}
      }
      }
    }
    }
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

        ParticleBaseFormat q;
        q+=_P_jets_I1I_PTorderingfinalstate_REG_[ind[0]]->momentum();
        q+=_P_jets_I2I_PTorderingfinalstate_REG_[ind[1]]->momentum();
        if (q.m()>500.0) {filter[1]=true; break;}
      }
      }
    }
    }
    MAbool filter_global = (filter[0] && filter[1]);
    if(!Manager()->ApplyCut(filter_global, "2_sdETA ( jets[1] jets[2] ) > 2.6 and M ( jets[1] jets[2] ) > 500.0")) return true;
  }

  return true;
}

void user::Finalize(const SampleFormat& summary, const std::vector<SampleFormat>& files)
{
}
