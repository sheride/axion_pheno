void selection_9()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo19","canvas_plotflow_tempo19",0,0,1000,500);
  gStyle->SetOptStat(0);
  gStyle->SetOptTitle(0);
  canvas->SetHighLightColor(2);
  canvas->SetFillColor(0);
  canvas->SetBorderMode(0);
  canvas->SetBorderSize(3);
  canvas->SetFrameBorderMode(0);
  canvas->SetFrameBorderSize(0);
  canvas->SetTickx(1);
  canvas->SetTicky(1);
  canvas->SetLeftMargin(0.14);
  canvas->SetRightMargin(0.3);
  canvas->SetBottomMargin(0.15);
  canvas->SetTopMargin(0.05);

  // Creating a new TH1F
  TH1F* S10_M_0 = new TH1F("S10_M_0","S10_M_0",40,500.0,4000.0);
  // Content
  S10_M_0->SetBinContent(0,0.0); // underflow
  S10_M_0->SetBinContent(1,176.46067525);
  S10_M_0->SetBinContent(2,232.052410604);
  S10_M_0->SetBinContent(3,227.276021003);
  S10_M_0->SetBinContent(4,232.052410604);
  S10_M_0->SetBinContent(5,222.234281424);
  S10_M_0->SetBinContent(6,205.915002788);
  S10_M_0->SetBinContent(7,201.271303177);
  S10_M_0->SetBinContent(8,186.27877443);
  S10_M_0->SetBinContent(9,178.848855051);
  S10_M_0->SetBinContent(10,169.030725871);
  S10_M_0->SetBinContent(11,147.27166769);
  S10_M_0->SetBinContent(12,131.350429021);
  S10_M_0->SetBinContent(13,121.797649819);
  S10_M_0->SetBinContent(14,113.571680507);
  S10_M_0->SetBinContent(15,103.355541361);
  S10_M_0->SetBinContent(16,89.2917525365);
  S10_M_0->SetBinContent(17,93.2720622038);
  S10_M_0->SetBinContent(18,77.7488335013);
  S10_M_0->SetBinContent(19,65.1445145548);
  S10_M_0->SetBinContent(20,60.3681249541);
  S10_M_0->SetBinContent(21,61.4295248654);
  S10_M_0->SetBinContent(22,51.7441156749);
  S10_M_0->SetBinContent(23,50.0192958191);
  S10_M_0->SetBinContent(24,40.0685066508);
  S10_M_0->SetBinContent(25,35.8228470057);
  S10_M_0->SetBinContent(26,35.9555069946);
  S10_M_0->SetBinContent(27,30.6484174382);
  S10_M_0->SetBinContent(28,29.9850454937);
  S10_M_0->SetBinContent(29,27.7295316822);
  S10_M_0->SetBinContent(30,21.3610272145);
  S10_M_0->SetBinContent(31,19.238191392);
  S10_M_0->SetBinContent(32,19.105516403);
  S10_M_0->SetBinContent(33,16.8500025916);
  S10_M_0->SetBinContent(34,13.9311048356);
  S10_M_0->SetBinContent(35,14.9925227468);
  S10_M_0->SetBinContent(36,10.8795290906);
  S10_M_0->SetBinContent(37,9.42008021261);
  S10_M_0->SetBinContent(38,7.69527835678);
  S10_M_0->SetBinContent(39,9.2874022237);
  S10_M_0->SetBinContent(40,8.49134029024);
  S10_M_0->SetBinContent(41,53.8669454975); // overflow
  S10_M_0->SetEntries(27157);
  // Style
  S10_M_0->SetLineColor(1);
  S10_M_0->SetLineStyle(1);
  S10_M_0->SetLineWidth(1);
  S10_M_0->SetFillColor(0);
  S10_M_0->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S10_M_1 = new TH1F("S10_M_1","S10_M_1",40,500.0,4000.0);
  // Content
  S10_M_1->SetBinContent(0,0.0); // underflow
  S10_M_1->SetBinContent(1,115.567907729);
  S10_M_1->SetBinContent(2,144.897843886);
  S10_M_1->SetBinContent(3,152.751928136);
  S10_M_1->SetBinContent(4,149.067048438);
  S10_M_1->SetBinContent(5,143.531290601);
  S10_M_1->SetBinContent(6,136.480357665);
  S10_M_1->SetBinContent(7,130.473794223);
  S10_M_1->SetBinContent(8,119.981148218);
  S10_M_1->SetBinContent(9,113.957198602);
  S10_M_1->SetBinContent(10,98.5779585291);
  S10_M_1->SetBinContent(11,90.4830457908);
  S10_M_1->SetBinContent(12,90.8901820267);
  S10_M_1->SetBinContent(13,83.7485412245);
  S10_M_1->SetBinContent(14,73.3281377701);
  S10_M_1->SetBinContent(15,70.5274949061);
  S10_M_1->SetBinContent(16,61.1474141631);
  S10_M_1->SetBinContent(17,59.8678217245);
  S10_M_1->SetBinContent(18,52.4949148305);
  S10_M_1->SetBinContent(19,44.2419078124);
  S10_M_1->SetBinContent(20,42.1538582777);
  S10_M_1->SetBinContent(21,36.0664791023);
  S10_M_1->SetBinContent(22,32.3783320021);
  S10_M_1->SetBinContent(23,31.2561443916);
  S10_M_1->SetBinContent(24,25.4042639422);
  S10_M_1->SetBinContent(25,25.9668775389);
  S10_M_1->SetBinContent(26,21.9576048052);
  S10_M_1->SetBinContent(27,21.8785936367);
  S10_M_1->SetBinContent(28,19.2353256245);
  S10_M_1->SetBinContent(29,15.8695871375);
  S10_M_1->SetBinContent(30,15.5470556221);
  S10_M_1->SetBinContent(31,14.1043658823);
  S10_M_1->SetBinContent(32,13.7852486517);
  S10_M_1->SetBinContent(33,11.7020462624);
  S10_M_1->SetBinContent(34,9.6181694094);
  S10_M_1->SetBinContent(35,8.73569817092);
  S10_M_1->SetBinContent(36,7.93241196268);
  S10_M_1->SetBinContent(37,6.8117201627);
  S10_M_1->SetBinContent(38,5.60960411316);
  S10_M_1->SetBinContent(39,5.6095561513);
  S10_M_1->SetBinContent(40,4.40845329605);
  S10_M_1->SetBinContent(41,33.7369715805); // overflow
  S10_M_1->SetEntries(29220);
  // Style
  S10_M_1->SetLineColor(2);
  S10_M_1->SetLineStyle(1);
  S10_M_1->SetLineWidth(1);
  S10_M_1->SetFillColor(0);
  S10_M_1->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S10_M_2 = new TH1F("S10_M_2","S10_M_2",40,500.0,4000.0);
  // Content
  S10_M_2->SetBinContent(0,0.0); // underflow
  S10_M_2->SetBinContent(1,79.6374791156);
  S10_M_2->SetBinContent(2,95.6795629663);
  S10_M_2->SetBinContent(3,103.336014804);
  S10_M_2->SetBinContent(4,102.867234692);
  S10_M_2->SetBinContent(5,98.6483936789);
  S10_M_2->SetBinContent(6,95.6795629663);
  S10_M_2->SetBinContent(7,88.700211291);
  S10_M_2->SetBinContent(8,84.0125901658);
  S10_M_2->SetBinContent(9,76.5124083655);
  S10_M_2->SetBinContent(10,72.3456173653);
  S10_M_2->SetBinContent(11,64.6891655275);
  S10_M_2->SetBinContent(12,57.8660838898);
  S10_M_2->SetBinContent(13,51.667992402);
  S10_M_2->SetBinContent(14,46.2511911018);
  S10_M_2->SetBinContent(15,46.3553511268);
  S10_M_2->SetBinContent(16,42.2406701392);
  S10_M_2->SetBinContent(17,35.7300985764);
  S10_M_2->SetBinContent(18,33.8550381263);
  S10_M_2->SetBinContent(19,32.5008378013);
  S10_M_2->SetBinContent(20,29.1674200011);
  S10_M_2->SetBinContent(21,26.042340251);
  S10_M_2->SetBinContent(22,22.1880743259);
  S10_M_2->SetBinContent(23,22.5005814009);
  S10_M_2->SetBinContent(24,18.8546535257);
  S10_M_2->SetBinContent(25,17.6046222257);
  S10_M_2->SetBinContent(26,15.1566426381);
  S10_M_2->SetBinContent(27,13.8545253255);
  S10_M_2->SetBinContent(28,11.6669698005);
  S10_M_2->SetBinContent(29,11.3023767129);
  S10_M_2->SetBinContent(30,10.6252735504);
  S10_M_2->SetBinContent(31,8.75022510034);
  S10_M_2->SetBinContent(32,8.28146298783);
  S10_M_2->SetBinContent(33,6.66683860026);
  S10_M_2->SetBinContent(34,6.66683860026);
  S10_M_2->SetBinContent(35,5.46889031272);
  S10_M_2->SetBinContent(36,4.84387616269);
  S10_M_2->SetBinContent(37,4.53136608768);
  S10_M_2->SetBinContent(38,4.37511405017);
  S10_M_2->SetBinContent(39,3.59384186264);
  S10_M_2->SetBinContent(40,3.69801088765);
  S10_M_2->SetBinContent(41,22.8651744884); // overflow
  S10_M_2->SetEntries(30475);
  // Style
  S10_M_2->SetLineColor(3);
  S10_M_2->SetLineStyle(1);
  S10_M_2->SetLineWidth(1);
  S10_M_2->SetFillColor(0);
  S10_M_2->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S10_M_3 = new TH1F("S10_M_3","S10_M_3",40,500.0,4000.0);
  // Content
  S10_M_3->SetBinContent(0,0.0); // underflow
  S10_M_3->SetBinContent(1,56.3296971344);
  S10_M_3->SetBinContent(2,66.0024500767);
  S10_M_3->SetBinContent(3,71.3367216993);
  S10_M_3->SetBinContent(4,68.669570888);
  S10_M_3->SetBinContent(5,68.6340208771);
  S10_M_3->SetBinContent(6,66.2513901524);
  S10_M_3->SetBinContent(7,60.0636482702);
  S10_M_3->SetBinContent(8,58.4278377726);
  S10_M_3->SetBinContent(9,53.0224361284);
  S10_M_3->SetBinContent(10,50.568705382);
  S10_M_3->SetBinContent(11,46.5857841705);
  S10_M_3->SetBinContent(12,42.5673129482);
  S10_M_3->SetBinContent(13,39.6157020503);
  S10_M_3->SetBinContent(14,34.032520352);
  S10_M_3->SetBinContent(15,31.6498896273);
  S10_M_3->SetBinContent(16,29.9784871189);
  S10_M_3->SetBinContent(17,27.0624322319);
  S10_M_3->SetBinContent(18,25.2487846802);
  S10_M_3->SetBinContent(19,23.5062641502);
  S10_M_3->SetBinContent(20,19.3811098954);
  S10_M_3->SetBinContent(21,18.5987546574);
  S10_M_3->SetBinContent(22,15.8249448136);
  S10_M_3->SetBinContent(23,14.5091624134);
  S10_M_3->SetBinContent(24,12.8022008942);
  S10_M_3->SetBinContent(25,11.6997905589);
  S10_M_3->SetBinContent(26,11.4508564831);
  S10_M_3->SetBinContent(27,9.92170501799);
  S10_M_3->SetBinContent(28,8.25030850958);
  S10_M_3->SetBinContent(29,7.71688134733);
  S10_M_3->SetBinContent(30,7.00565013098);
  S10_M_3->SetBinContent(31,5.61874370911);
  S10_M_3->SetBinContent(32,6.57890900118);
  S10_M_3->SetBinContent(33,5.76099175238);
  S10_M_3->SetBinContent(34,4.80082646032);
  S10_M_3->SetBinContent(35,3.48504406008);
  S10_M_3->SetBinContent(36,3.59173009254);
  S10_M_3->SetBinContent(37,3.16498896273);
  S10_M_3->SetBinContent(38,2.77381014374);
  S10_M_3->SetBinContent(39,2.16926195985);
  S10_M_3->SetBinContent(40,1.99145340576);
  S10_M_3->SetBinContent(41,16.53617603); // overflow
  S10_M_3->SetEntries(31303);
  // Style
  S10_M_3->SetLineColor(4);
  S10_M_3->SetLineStyle(1);
  S10_M_3->SetLineWidth(1);
  S10_M_3->SetFillColor(0);
  S10_M_3->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S10_M_4 = new TH1F("S10_M_4","S10_M_4",40,500.0,4000.0);
  // Content
  S10_M_4->SetBinContent(0,0.0); // underflow
  S10_M_4->SetBinContent(1,0.0);
  S10_M_4->SetBinContent(2,0.0);
  S10_M_4->SetBinContent(3,0.0);
  S10_M_4->SetBinContent(4,0.0);
  S10_M_4->SetBinContent(5,0.0);
  S10_M_4->SetBinContent(6,0.0);
  S10_M_4->SetBinContent(7,0.0);
  S10_M_4->SetBinContent(8,0.0);
  S10_M_4->SetBinContent(9,0.0);
  S10_M_4->SetBinContent(10,0.0);
  S10_M_4->SetBinContent(11,0.0);
  S10_M_4->SetBinContent(12,0.0);
  S10_M_4->SetBinContent(13,0.0);
  S10_M_4->SetBinContent(14,0.0);
  S10_M_4->SetBinContent(15,0.0);
  S10_M_4->SetBinContent(16,0.0);
  S10_M_4->SetBinContent(17,0.0);
  S10_M_4->SetBinContent(18,0.0);
  S10_M_4->SetBinContent(19,0.0);
  S10_M_4->SetBinContent(20,0.0);
  S10_M_4->SetBinContent(21,0.0);
  S10_M_4->SetBinContent(22,0.0);
  S10_M_4->SetBinContent(23,0.0);
  S10_M_4->SetBinContent(24,0.0);
  S10_M_4->SetBinContent(25,0.0);
  S10_M_4->SetBinContent(26,0.0);
  S10_M_4->SetBinContent(27,0.0);
  S10_M_4->SetBinContent(28,0.0);
  S10_M_4->SetBinContent(29,0.0);
  S10_M_4->SetBinContent(30,0.0);
  S10_M_4->SetBinContent(31,0.0);
  S10_M_4->SetBinContent(32,0.0);
  S10_M_4->SetBinContent(33,0.0);
  S10_M_4->SetBinContent(34,0.0);
  S10_M_4->SetBinContent(35,0.0);
  S10_M_4->SetBinContent(36,0.0);
  S10_M_4->SetBinContent(37,0.0);
  S10_M_4->SetBinContent(38,0.0);
  S10_M_4->SetBinContent(39,0.0);
  S10_M_4->SetBinContent(40,0.0);
  S10_M_4->SetBinContent(41,0.0); // overflow
  S10_M_4->SetEntries(0);
  // Style
  S10_M_4->SetLineColor(5);
  S10_M_4->SetLineStyle(1);
  S10_M_4->SetLineWidth(1);
  S10_M_4->SetFillColor(0);
  S10_M_4->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S10_M_5 = new TH1F("S10_M_5","S10_M_5",40,500.0,4000.0);
  // Content
  S10_M_5->SetBinContent(0,0.0); // underflow
  S10_M_5->SetBinContent(1,0.0);
  S10_M_5->SetBinContent(2,78.9085275503);
  S10_M_5->SetBinContent(3,158.069001296);
  S10_M_5->SetBinContent(4,0.0);
  S10_M_5->SetBinContent(5,0.0);
  S10_M_5->SetBinContent(6,0.0);
  S10_M_5->SetBinContent(7,0.0);
  S10_M_5->SetBinContent(8,0.0);
  S10_M_5->SetBinContent(9,0.0);
  S10_M_5->SetBinContent(10,0.0);
  S10_M_5->SetBinContent(11,0.0);
  S10_M_5->SetBinContent(12,0.0);
  S10_M_5->SetBinContent(13,0.0);
  S10_M_5->SetBinContent(14,0.0);
  S10_M_5->SetBinContent(15,0.0);
  S10_M_5->SetBinContent(16,0.0);
  S10_M_5->SetBinContent(17,0.0);
  S10_M_5->SetBinContent(18,0.0);
  S10_M_5->SetBinContent(19,0.0);
  S10_M_5->SetBinContent(20,0.0);
  S10_M_5->SetBinContent(21,0.0);
  S10_M_5->SetBinContent(22,0.0);
  S10_M_5->SetBinContent(23,0.0);
  S10_M_5->SetBinContent(24,0.0);
  S10_M_5->SetBinContent(25,0.0);
  S10_M_5->SetBinContent(26,0.0);
  S10_M_5->SetBinContent(27,0.0);
  S10_M_5->SetBinContent(28,0.0);
  S10_M_5->SetBinContent(29,0.0);
  S10_M_5->SetBinContent(30,0.0);
  S10_M_5->SetBinContent(31,0.0);
  S10_M_5->SetBinContent(32,0.0);
  S10_M_5->SetBinContent(33,0.0);
  S10_M_5->SetBinContent(34,0.0);
  S10_M_5->SetBinContent(35,0.0);
  S10_M_5->SetBinContent(36,0.0);
  S10_M_5->SetBinContent(37,0.0);
  S10_M_5->SetBinContent(38,0.0);
  S10_M_5->SetBinContent(39,0.0);
  S10_M_5->SetBinContent(40,0.0);
  S10_M_5->SetBinContent(41,0.0); // overflow
  S10_M_5->SetEntries(3);
  // Style
  S10_M_5->SetLineColor(6);
  S10_M_5->SetLineStyle(1);
  S10_M_5->SetLineWidth(1);
  S10_M_5->SetFillColor(0);
  S10_M_5->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S10_M_6 = new TH1F("S10_M_6","S10_M_6",40,500.0,4000.0);
  // Content
  S10_M_6->SetBinContent(0,0.0); // underflow
  S10_M_6->SetBinContent(1,431.886384623);
  S10_M_6->SetBinContent(2,345.468298229);
  S10_M_6->SetBinContent(3,259.23296102);
  S10_M_6->SetBinContent(4,69.0686148513);
  S10_M_6->SetBinContent(5,69.102565102);
  S10_M_6->SetBinContent(6,17.3004886513);
  S10_M_6->SetBinContent(7,34.5703759645);
  S10_M_6->SetBinContent(8,17.2486900217);
  S10_M_6->SetBinContent(9,51.8012233715);
  S10_M_6->SetBinContent(10,34.5060779939);
  S10_M_6->SetBinContent(11,17.3004886513);
  S10_M_6->SetBinContent(12,0.0);
  S10_M_6->SetBinContent(13,17.2964768729);
  S10_M_6->SetBinContent(14,17.2596417155);
  S10_M_6->SetBinContent(15,34.5442071804);
  S10_M_6->SetBinContent(16,0.0);
  S10_M_6->SetBinContent(17,0.0);
  S10_M_6->SetBinContent(18,0.0);
  S10_M_6->SetBinContent(19,0.0);
  S10_M_6->SetBinContent(20,0.0);
  S10_M_6->SetBinContent(21,0.0);
  S10_M_6->SetBinContent(22,0.0);
  S10_M_6->SetBinContent(23,0.0);
  S10_M_6->SetBinContent(24,0.0);
  S10_M_6->SetBinContent(25,0.0);
  S10_M_6->SetBinContent(26,17.2515144059);
  S10_M_6->SetBinContent(27,0.0);
  S10_M_6->SetBinContent(28,0.0);
  S10_M_6->SetBinContent(29,0.0);
  S10_M_6->SetBinContent(30,0.0);
  S10_M_6->SetBinContent(31,0.0);
  S10_M_6->SetBinContent(32,0.0);
  S10_M_6->SetBinContent(33,0.0);
  S10_M_6->SetBinContent(34,0.0);
  S10_M_6->SetBinContent(35,0.0);
  S10_M_6->SetBinContent(36,0.0);
  S10_M_6->SetBinContent(37,0.0);
  S10_M_6->SetBinContent(38,0.0);
  S10_M_6->SetBinContent(39,0.0);
  S10_M_6->SetBinContent(40,0.0);
  S10_M_6->SetBinContent(41,0.0); // overflow
  S10_M_6->SetEntries(83);
  // Style
  S10_M_6->SetLineColor(7);
  S10_M_6->SetLineStyle(1);
  S10_M_6->SetLineWidth(1);
  S10_M_6->SetFillColor(0);
  S10_M_6->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S10_M_7 = new TH1F("S10_M_7","S10_M_7",40,500.0,4000.0);
  // Content
  S10_M_7->SetBinContent(0,0.0); // underflow
  S10_M_7->SetBinContent(1,303.232533396);
  S10_M_7->SetBinContent(2,180.660599217);
  S10_M_7->SetBinContent(3,139.153907595);
  S10_M_7->SetBinContent(4,66.4489221758);
  S10_M_7->SetBinContent(5,51.9282705759);
  S10_M_7->SetBinContent(6,37.3800954483);
  S10_M_7->SetBinContent(7,49.8790083346);
  S10_M_7->SetBinContent(8,16.6057550138);
  S10_M_7->SetBinContent(9,12.4565024189);
  S10_M_7->SetBinContent(10,4.15832324172);
  S10_M_7->SetBinContent(11,14.5418193277);
  S10_M_7->SetBinContent(12,10.3750543834);
  S10_M_7->SetBinContent(13,6.22338410345);
  S10_M_7->SetBinContent(14,8.3041368381);
  S10_M_7->SetBinContent(15,2.07715246103);
  S10_M_7->SetBinContent(16,2.0802989138);
  S10_M_7->SetBinContent(17,2.07522090947);
  S10_M_7->SetBinContent(18,0.0);
  S10_M_7->SetBinContent(19,4.1490939162);
  S10_M_7->SetBinContent(20,2.07028600441);
  S10_M_7->SetBinContent(21,0.0);
  S10_M_7->SetBinContent(22,2.07793921848);
  S10_M_7->SetBinContent(23,0.0);
  S10_M_7->SetBinContent(24,2.0794792666);
  S10_M_7->SetBinContent(25,0.0);
  S10_M_7->SetBinContent(26,0.0);
  S10_M_7->SetBinContent(27,0.0);
  S10_M_7->SetBinContent(28,2.07697012487);
  S10_M_7->SetBinContent(29,0.0);
  S10_M_7->SetBinContent(30,0.0);
  S10_M_7->SetBinContent(31,0.0);
  S10_M_7->SetBinContent(32,0.0);
  S10_M_7->SetBinContent(33,0.0);
  S10_M_7->SetBinContent(34,0.0);
  S10_M_7->SetBinContent(35,0.0);
  S10_M_7->SetBinContent(36,0.0);
  S10_M_7->SetBinContent(37,0.0);
  S10_M_7->SetBinContent(38,0.0);
  S10_M_7->SetBinContent(39,0.0);
  S10_M_7->SetBinContent(40,0.0);
  S10_M_7->SetBinContent(41,0.0); // overflow
  S10_M_7->SetEntries(443);
  // Style
  S10_M_7->SetLineColor(8);
  S10_M_7->SetLineStyle(1);
  S10_M_7->SetLineWidth(1);
  S10_M_7->SetFillColor(0);
  S10_M_7->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S10_M_8 = new TH1F("S10_M_8","S10_M_8",40,500.0,4000.0);
  // Content
  S10_M_8->SetBinContent(0,0.0); // underflow
  S10_M_8->SetBinContent(1,77.1216332539);
  S10_M_8->SetBinContent(2,62.0060265446);
  S10_M_8->SetBinContent(3,34.0337768278);
  S10_M_8->SetBinContent(4,22.6840791223);
  S10_M_8->SetBinContent(5,15.1173864029);
  S10_M_8->SetBinContent(6,7.56154935934);
  S10_M_8->SetBinContent(7,9.07259569428);
  S10_M_8->SetBinContent(8,7.56377511423);
  S10_M_8->SetBinContent(9,10.5877658205);
  S10_M_8->SetBinContent(10,5.29293161623);
  S10_M_8->SetBinContent(11,2.27210475911);
  S10_M_8->SetBinContent(12,1.51369994456);
  S10_M_8->SetBinContent(13,3.77981837884);
  S10_M_8->SetBinContent(14,3.02303577093);
  S10_M_8->SetBinContent(15,0.0);
  S10_M_8->SetBinContent(16,0.754445792862);
  S10_M_8->SetBinContent(17,1.51069904435);
  S10_M_8->SetBinContent(18,1.51297987416);
  S10_M_8->SetBinContent(19,0.751764418205);
  S10_M_8->SetBinContent(20,1.51367035886);
  S10_M_8->SetBinContent(21,0.756398448995);
  S10_M_8->SetBinContent(22,0.0);
  S10_M_8->SetBinContent(23,0.0);
  S10_M_8->SetBinContent(24,0.0);
  S10_M_8->SetBinContent(25,0.757503588643);
  S10_M_8->SetBinContent(26,0.0);
  S10_M_8->SetBinContent(27,0.0);
  S10_M_8->SetBinContent(28,0.0);
  S10_M_8->SetBinContent(29,0.757313785005);
  S10_M_8->SetBinContent(30,0.0);
  S10_M_8->SetBinContent(31,0.0);
  S10_M_8->SetBinContent(32,0.0);
  S10_M_8->SetBinContent(33,0.0);
  S10_M_8->SetBinContent(34,0.0);
  S10_M_8->SetBinContent(35,0.0);
  S10_M_8->SetBinContent(36,0.0);
  S10_M_8->SetBinContent(37,0.0);
  S10_M_8->SetBinContent(38,0.0);
  S10_M_8->SetBinContent(39,0.0);
  S10_M_8->SetBinContent(40,0.0);
  S10_M_8->SetBinContent(41,0.0); // overflow
  S10_M_8->SetEntries(357);
  // Style
  S10_M_8->SetLineColor(9);
  S10_M_8->SetLineStyle(1);
  S10_M_8->SetLineWidth(1);
  S10_M_8->SetFillColor(0);
  S10_M_8->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S10_M_9 = new TH1F("S10_M_9","S10_M_9",40,500.0,4000.0);
  // Content
  S10_M_9->SetBinContent(0,0.0); // underflow
  S10_M_9->SetBinContent(1,30.9752704771);
  S10_M_9->SetBinContent(2,18.890676357);
  S10_M_9->SetBinContent(3,15.9121277006);
  S10_M_9->SetBinContent(4,11.2458155059);
  S10_M_9->SetBinContent(5,8.06650235642);
  S10_M_9->SetBinContent(6,5.51680339371);
  S10_M_9->SetBinContent(7,4.6678069272);
  S10_M_9->SetBinContent(8,3.39409869423);
  S10_M_9->SetBinContent(9,2.54627088916);
  S10_M_9->SetBinContent(10,2.33445201308);
  S10_M_9->SetBinContent(11,1.69784057419);
  S10_M_9->SetBinContent(12,1.48398418739);
  S10_M_9->SetBinContent(13,0.424144172122);
  S10_M_9->SetBinContent(14,0.42396642016);
  S10_M_9->SetBinContent(15,0.211939522341);
  S10_M_9->SetBinContent(16,0.0);
  S10_M_9->SetBinContent(17,0.212060774573);
  S10_M_9->SetBinContent(18,1.06150326577);
  S10_M_9->SetBinContent(19,0.211939522341);
  S10_M_9->SetBinContent(20,0.211760962415);
  S10_M_9->SetBinContent(21,0.0);
  S10_M_9->SetBinContent(22,0.424843637636);
  S10_M_9->SetBinContent(23,0.212260572395);
  S10_M_9->SetBinContent(24,0.0);
  S10_M_9->SetBinContent(25,0.0);
  S10_M_9->SetBinContent(26,0.0);
  S10_M_9->SetBinContent(27,0.0);
  S10_M_9->SetBinContent(28,0.211607074231);
  S10_M_9->SetBinContent(29,0.0);
  S10_M_9->SetBinContent(30,0.0);
  S10_M_9->SetBinContent(31,0.0);
  S10_M_9->SetBinContent(32,0.0);
  S10_M_9->SetBinContent(33,0.0);
  S10_M_9->SetBinContent(34,0.0);
  S10_M_9->SetBinContent(35,0.0);
  S10_M_9->SetBinContent(36,0.0);
  S10_M_9->SetBinContent(37,0.0);
  S10_M_9->SetBinContent(38,0.0);
  S10_M_9->SetBinContent(39,0.0);
  S10_M_9->SetBinContent(40,0.0);
  S10_M_9->SetBinContent(41,0.0); // overflow
  S10_M_9->SetEntries(520);
  // Style
  S10_M_9->SetLineColor(10);
  S10_M_9->SetLineStyle(1);
  S10_M_9->SetLineWidth(1);
  S10_M_9->SetFillColor(0);
  S10_M_9->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S10_M_10 = new TH1F("S10_M_10","S10_M_10",40,500.0,4000.0);
  // Content
  S10_M_10->SetBinContent(0,0.0); // underflow
  S10_M_10->SetBinContent(1,1.71197029584);
  S10_M_10->SetBinContent(2,1.48402463275);
  S10_M_10->SetBinContent(3,0.800874885228);
  S10_M_10->SetBinContent(4,0.229337431742);
  S10_M_10->SetBinContent(5,0.802187585187);
  S10_M_10->SetBinContent(6,0.685610539175);
  S10_M_10->SetBinContent(7,0.0);
  S10_M_10->SetBinContent(8,0.685668776994);
  S10_M_10->SetBinContent(9,0.114337238966);
  S10_M_10->SetBinContent(10,0.114483321046);
  S10_M_10->SetBinContent(11,0.457163605358);
  S10_M_10->SetBinContent(12,0.0);
  S10_M_10->SetBinContent(13,0.113449045733);
  S10_M_10->SetBinContent(14,0.0);
  S10_M_10->SetBinContent(15,0.226898091465);
  S10_M_10->SetBinContent(16,0.0);
  S10_M_10->SetBinContent(17,0.0);
  S10_M_10->SetBinContent(18,0.227673975235);
  S10_M_10->SetBinContent(19,0.114071224206);
  S10_M_10->SetBinContent(20,0.0);
  S10_M_10->SetBinContent(21,0.115000192777);
  S10_M_10->SetBinContent(22,0.0);
  S10_M_10->SetBinContent(23,0.0);
  S10_M_10->SetBinContent(24,0.0);
  S10_M_10->SetBinContent(25,0.0);
  S10_M_10->SetBinContent(26,0.0);
  S10_M_10->SetBinContent(27,0.0);
  S10_M_10->SetBinContent(28,0.0);
  S10_M_10->SetBinContent(29,0.0);
  S10_M_10->SetBinContent(30,0.0);
  S10_M_10->SetBinContent(31,0.0);
  S10_M_10->SetBinContent(32,0.0);
  S10_M_10->SetBinContent(33,0.0);
  S10_M_10->SetBinContent(34,0.0);
  S10_M_10->SetBinContent(35,0.0);
  S10_M_10->SetBinContent(36,0.0);
  S10_M_10->SetBinContent(37,0.0);
  S10_M_10->SetBinContent(38,0.0);
  S10_M_10->SetBinContent(39,0.0);
  S10_M_10->SetBinContent(40,0.0);
  S10_M_10->SetBinContent(41,0.0); // overflow
  S10_M_10->SetEntries(69);
  // Style
  S10_M_10->SetLineColor(11);
  S10_M_10->SetLineStyle(1);
  S10_M_10->SetLineWidth(1);
  S10_M_10->SetFillColor(0);
  S10_M_10->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S10_M_11 = new TH1F("S10_M_11","S10_M_11",40,500.0,4000.0);
  // Content
  S10_M_11->SetBinContent(0,0.0); // underflow
  S10_M_11->SetBinContent(1,0.0947974410912);
  S10_M_11->SetBinContent(2,0.189590810973);
  S10_M_11->SetBinContent(3,0.0677245643041);
  S10_M_11->SetBinContent(4,0.0948292022973);
  S10_M_11->SetBinContent(5,0.0542057822538);
  S10_M_11->SetBinContent(6,0.0406224672073);
  S10_M_11->SetBinContent(7,0.0134999014569);
  S10_M_11->SetBinContent(8,0.0541923559257);
  S10_M_11->SetBinContent(9,0.0);
  S10_M_11->SetBinContent(10,0.0);
  S10_M_11->SetBinContent(11,0.027015495837);
  S10_M_11->SetBinContent(12,0.0135876316831);
  S10_M_11->SetBinContent(13,0.0135550735594);
  S10_M_11->SetBinContent(14,0.0);
  S10_M_11->SetBinContent(15,0.0135002710418);
  S10_M_11->SetBinContent(16,0.0);
  S10_M_11->SetBinContent(17,0.0135115924682);
  S10_M_11->SetBinContent(18,0.0135566269711);
  S10_M_11->SetBinContent(19,0.0);
  S10_M_11->SetBinContent(20,0.0);
  S10_M_11->SetBinContent(21,0.0135575220597);
  S10_M_11->SetBinContent(22,0.0135257781778);
  S10_M_11->SetBinContent(23,0.0);
  S10_M_11->SetBinContent(24,0.0);
  S10_M_11->SetBinContent(25,0.0);
  S10_M_11->SetBinContent(26,0.0);
  S10_M_11->SetBinContent(27,0.0);
  S10_M_11->SetBinContent(28,0.0);
  S10_M_11->SetBinContent(29,0.0);
  S10_M_11->SetBinContent(30,0.0);
  S10_M_11->SetBinContent(31,0.0);
  S10_M_11->SetBinContent(32,0.0);
  S10_M_11->SetBinContent(33,0.0);
  S10_M_11->SetBinContent(34,0.0);
  S10_M_11->SetBinContent(35,0.0);
  S10_M_11->SetBinContent(36,0.0);
  S10_M_11->SetBinContent(37,0.0);
  S10_M_11->SetBinContent(38,0.0);
  S10_M_11->SetBinContent(39,0.0);
  S10_M_11->SetBinContent(40,0.0);
  S10_M_11->SetBinContent(41,0.0); // overflow
  S10_M_11->SetEntries(54);
  // Style
  S10_M_11->SetLineColor(12);
  S10_M_11->SetLineStyle(1);
  S10_M_11->SetLineWidth(1);
  S10_M_11->SetFillColor(0);
  S10_M_11->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S10_M_12 = new TH1F("S10_M_12","S10_M_12",40,500.0,4000.0);
  // Content
  S10_M_12->SetBinContent(0,0.0); // underflow
  S10_M_12->SetBinContent(1,0.0);
  S10_M_12->SetBinContent(2,0.912787033803);
  S10_M_12->SetBinContent(3,0.0);
  S10_M_12->SetBinContent(4,0.909306167943);
  S10_M_12->SetBinContent(5,0.913150150035);
  S10_M_12->SetBinContent(6,0.0);
  S10_M_12->SetBinContent(7,0.0);
  S10_M_12->SetBinContent(8,0.0);
  S10_M_12->SetBinContent(9,0.0);
  S10_M_12->SetBinContent(10,0.0);
  S10_M_12->SetBinContent(11,0.0);
  S10_M_12->SetBinContent(12,0.0);
  S10_M_12->SetBinContent(13,0.909853848219);
  S10_M_12->SetBinContent(14,0.0);
  S10_M_12->SetBinContent(15,0.0);
  S10_M_12->SetBinContent(16,0.0);
  S10_M_12->SetBinContent(17,0.0);
  S10_M_12->SetBinContent(18,0.0);
  S10_M_12->SetBinContent(19,0.0);
  S10_M_12->SetBinContent(20,0.0);
  S10_M_12->SetBinContent(21,0.0);
  S10_M_12->SetBinContent(22,0.0);
  S10_M_12->SetBinContent(23,0.0);
  S10_M_12->SetBinContent(24,0.0);
  S10_M_12->SetBinContent(25,0.0);
  S10_M_12->SetBinContent(26,0.0);
  S10_M_12->SetBinContent(27,0.0);
  S10_M_12->SetBinContent(28,0.0);
  S10_M_12->SetBinContent(29,0.0);
  S10_M_12->SetBinContent(30,0.0);
  S10_M_12->SetBinContent(31,0.0);
  S10_M_12->SetBinContent(32,0.0);
  S10_M_12->SetBinContent(33,0.0);
  S10_M_12->SetBinContent(34,0.0);
  S10_M_12->SetBinContent(35,0.0);
  S10_M_12->SetBinContent(36,0.0);
  S10_M_12->SetBinContent(37,0.0);
  S10_M_12->SetBinContent(38,0.0);
  S10_M_12->SetBinContent(39,0.0);
  S10_M_12->SetBinContent(40,0.0);
  S10_M_12->SetBinContent(41,0.0); // overflow
  S10_M_12->SetEntries(4);
  // Style
  S10_M_12->SetLineColor(13);
  S10_M_12->SetLineStyle(1);
  S10_M_12->SetLineWidth(1);
  S10_M_12->SetFillColor(0);
  S10_M_12->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S10_M_13 = new TH1F("S10_M_13","S10_M_13",40,500.0,4000.0);
  // Content
  S10_M_13->SetBinContent(0,0.0); // underflow
  S10_M_13->SetBinContent(1,14.3002261044);
  S10_M_13->SetBinContent(2,15.815033764);
  S10_M_13->SetBinContent(3,12.8022151729);
  S10_M_13->SetBinContent(4,12.8052739128);
  S10_M_13->SetBinContent(5,5.2694745129);
  S10_M_13->SetBinContent(6,6.02194933975);
  S10_M_13->SetBinContent(7,4.51375190541);
  S10_M_13->SetBinContent(8,1.50452787608);
  S10_M_13->SetBinContent(9,3.76368812183);
  S10_M_13->SetBinContent(10,6.03187862333);
  S10_M_13->SetBinContent(11,2.26192271872);
  S10_M_13->SetBinContent(12,0.751971234906);
  S10_M_13->SetBinContent(13,1.5068211563);
  S10_M_13->SetBinContent(14,0.0);
  S10_M_13->SetBinContent(15,0.0);
  S10_M_13->SetBinContent(16,0.0);
  S10_M_13->SetBinContent(17,0.0);
  S10_M_13->SetBinContent(18,0.0);
  S10_M_13->SetBinContent(19,0.0);
  S10_M_13->SetBinContent(20,0.0);
  S10_M_13->SetBinContent(21,0.0);
  S10_M_13->SetBinContent(22,0.0);
  S10_M_13->SetBinContent(23,0.0);
  S10_M_13->SetBinContent(24,0.0);
  S10_M_13->SetBinContent(25,0.0);
  S10_M_13->SetBinContent(26,0.0);
  S10_M_13->SetBinContent(27,0.0);
  S10_M_13->SetBinContent(28,0.0);
  S10_M_13->SetBinContent(29,0.0);
  S10_M_13->SetBinContent(30,0.0);
  S10_M_13->SetBinContent(31,0.0);
  S10_M_13->SetBinContent(32,0.0);
  S10_M_13->SetBinContent(33,0.0);
  S10_M_13->SetBinContent(34,0.0);
  S10_M_13->SetBinContent(35,0.0);
  S10_M_13->SetBinContent(36,0.0);
  S10_M_13->SetBinContent(37,0.0);
  S10_M_13->SetBinContent(38,0.0);
  S10_M_13->SetBinContent(39,0.0);
  S10_M_13->SetBinContent(40,0.0);
  S10_M_13->SetBinContent(41,0.0); // overflow
  S10_M_13->SetEntries(116);
  // Style
  S10_M_13->SetLineColor(14);
  S10_M_13->SetLineStyle(1);
  S10_M_13->SetLineWidth(1);
  S10_M_13->SetFillColor(0);
  S10_M_13->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S10_M_14 = new TH1F("S10_M_14","S10_M_14",40,500.0,4000.0);
  // Content
  S10_M_14->SetBinContent(0,0.0); // underflow
  S10_M_14->SetBinContent(1,116.750461706);
  S10_M_14->SetBinContent(2,80.8489064136);
  S10_M_14->SetBinContent(3,70.1332998558);
  S10_M_14->SetBinContent(4,42.4900910105);
  S10_M_14->SetBinContent(5,40.0147321172);
  S10_M_14->SetBinContent(6,25.1574599103);
  S10_M_14->SetBinContent(7,22.2769472802);
  S10_M_14->SetBinContent(8,11.1408395836);
  S10_M_14->SetBinContent(9,8.25449817055);
  S10_M_14->SetBinContent(10,10.3113638539);
  S10_M_14->SetBinContent(11,5.77703689351);
  S10_M_14->SetBinContent(12,5.36263266782);
  S10_M_14->SetBinContent(13,1.23823276966);
  S10_M_14->SetBinContent(14,3.30095587715);
  S10_M_14->SetBinContent(15,2.06156314007);
  S10_M_14->SetBinContent(16,1.23641679755);
  S10_M_14->SetBinContent(17,1.65109981761);
  S10_M_14->SetBinContent(18,0.412044376027);
  S10_M_14->SetBinContent(19,1.23757767905);
  S10_M_14->SetBinContent(20,0.0);
  S10_M_14->SetBinContent(21,0.0);
  S10_M_14->SetBinContent(22,0.0);
  S10_M_14->SetBinContent(23,0.82497662835);
  S10_M_14->SetBinContent(24,0.410615973805);
  S10_M_14->SetBinContent(25,0.0);
  S10_M_14->SetBinContent(26,0.41322963299);
  S10_M_14->SetBinContent(27,0.824565901772);
  S10_M_14->SetBinContent(28,0.412044376027);
  S10_M_14->SetBinContent(29,0.0);
  S10_M_14->SetBinContent(30,0.413566319094);
  S10_M_14->SetBinContent(31,0.41219855084);
  S10_M_14->SetBinContent(32,0.0);
  S10_M_14->SetBinContent(33,0.0);
  S10_M_14->SetBinContent(34,0.0);
  S10_M_14->SetBinContent(35,0.0);
  S10_M_14->SetBinContent(36,0.0);
  S10_M_14->SetBinContent(37,0.0);
  S10_M_14->SetBinContent(38,0.0);
  S10_M_14->SetBinContent(39,0.0);
  S10_M_14->SetBinContent(40,0.0);
  S10_M_14->SetBinContent(41,0.0); // overflow
  S10_M_14->SetEntries(1099);
  // Style
  S10_M_14->SetLineColor(15);
  S10_M_14->SetLineStyle(1);
  S10_M_14->SetLineWidth(1);
  S10_M_14->SetFillColor(0);
  S10_M_14->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S10_M_15 = new TH1F("S10_M_15","S10_M_15",40,500.0,4000.0);
  // Content
  S10_M_15->SetBinContent(0,0.0); // underflow
  S10_M_15->SetBinContent(1,105.173460652);
  S10_M_15->SetBinContent(2,69.0559589939);
  S10_M_15->SetBinContent(3,46.0369352292);
  S10_M_15->SetBinContent(4,29.3067519022);
  S10_M_15->SetBinContent(5,22.9470880002);
  S10_M_15->SetBinContent(6,16.650686927);
  S10_M_15->SetBinContent(7,10.5847995603);
  S10_M_15->SetBinContent(8,8.21429230764);
  S10_M_15->SetBinContent(9,7.32695928663);
  S10_M_15->SetBinContent(10,4.44075055386);
  S10_M_15->SetBinContent(11,2.81293009119);
  S10_M_15->SetBinContent(12,2.29547057539);
  S10_M_15->SetBinContent(13,1.70226882325);
  S10_M_15->SetBinContent(14,1.77636876329);
  S10_M_15->SetBinContent(15,0.888337097464);
  S10_M_15->SetBinContent(16,0.888376478905);
  S10_M_15->SetBinContent(17,0.51800875163);
  S10_M_15->SetBinContent(18,0.221967753398);
  S10_M_15->SetBinContent(19,0.148049990104);
  S10_M_15->SetBinContent(20,0.222051747099);
  S10_M_15->SetBinContent(21,0.147781595058);
  S10_M_15->SetBinContent(22,0.295865525351);
  S10_M_15->SetBinContent(23,0.0741429590035);
  S10_M_15->SetBinContent(24,0.22238964588);
  S10_M_15->SetBinContent(25,0.0739651412732);
  S10_M_15->SetBinContent(26,0.148190380434);
  S10_M_15->SetBinContent(27,0.0);
  S10_M_15->SetBinContent(28,0.147762415394);
  S10_M_15->SetBinContent(29,0.0);
  S10_M_15->SetBinContent(30,0.0740800388835);
  S10_M_15->SetBinContent(31,0.0);
  S10_M_15->SetBinContent(32,0.148067606535);
  S10_M_15->SetBinContent(33,0.147993743785);
  S10_M_15->SetBinContent(34,0.0);
  S10_M_15->SetBinContent(35,0.0);
  S10_M_15->SetBinContent(36,0.073932583944);
  S10_M_15->SetBinContent(37,0.0);
  S10_M_15->SetBinContent(38,0.0);
  S10_M_15->SetBinContent(39,0.0);
  S10_M_15->SetBinContent(40,0.0);
  S10_M_15->SetBinContent(41,0.0); // overflow
  S10_M_15->SetEntries(4496);
  // Style
  S10_M_15->SetLineColor(16);
  S10_M_15->SetLineStyle(1);
  S10_M_15->SetLineWidth(1);
  S10_M_15->SetFillColor(0);
  S10_M_15->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S10_M_16 = new TH1F("S10_M_16","S10_M_16",40,500.0,4000.0);
  // Content
  S10_M_16->SetBinContent(0,0.0); // underflow
  S10_M_16->SetBinContent(1,36.071649539);
  S10_M_16->SetBinContent(2,23.7445032819);
  S10_M_16->SetBinContent(3,17.4691217867);
  S10_M_16->SetBinContent(4,12.3831779762);
  S10_M_16->SetBinContent(5,8.6965177207);
  S10_M_16->SetBinContent(6,6.29554415168);
  S10_M_16->SetBinContent(7,4.44296843017);
  S10_M_16->SetBinContent(8,3.53588295645);
  S10_M_16->SetBinContent(9,2.64753203852);
  S10_M_16->SetBinContent(10,1.81479152153);
  S10_M_16->SetBinContent(11,1.19137832922);
  S10_M_16->SetBinContent(12,1.07795040816);
  S10_M_16->SetBinContent(13,0.945233675814);
  S10_M_16->SetBinContent(14,0.661670925132);
  S10_M_16->SetBinContent(15,0.567417483276);
  S10_M_16->SetBinContent(16,0.283617876147);
  S10_M_16->SetBinContent(17,0.321355353017);
  S10_M_16->SetBinContent(18,0.245698908361);
  S10_M_16->SetBinContent(19,0.151245520412);
  S10_M_16->SetBinContent(20,0.11348814796);
  S10_M_16->SetBinContent(21,0.0756458816923);
  S10_M_16->SetBinContent(22,0.0567285746318);
  S10_M_16->SetBinContent(23,0.075619114183);
  S10_M_16->SetBinContent(24,0.0);
  S10_M_16->SetBinContent(25,0.0566696080894);
  S10_M_16->SetBinContent(26,0.0);
  S10_M_16->SetBinContent(27,0.0);
  S10_M_16->SetBinContent(28,0.0);
  S10_M_16->SetBinContent(29,0.0188733537298);
  S10_M_16->SetBinContent(30,0.0);
  S10_M_16->SetBinContent(31,0.0189064650189);
  S10_M_16->SetBinContent(32,0.0);
  S10_M_16->SetBinContent(33,0.0);
  S10_M_16->SetBinContent(34,0.0188968623249);
  S10_M_16->SetBinContent(35,0.0);
  S10_M_16->SetBinContent(36,0.0);
  S10_M_16->SetBinContent(37,0.0);
  S10_M_16->SetBinContent(38,0.0);
  S10_M_16->SetBinContent(39,0.0);
  S10_M_16->SetBinContent(40,0.0);
  S10_M_16->SetBinContent(41,0.0); // overflow
  S10_M_16->SetEntries(6505);
  // Style
  S10_M_16->SetLineColor(17);
  S10_M_16->SetLineStyle(1);
  S10_M_16->SetLineWidth(1);
  S10_M_16->SetFillColor(0);
  S10_M_16->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S10_M_17 = new TH1F("S10_M_17","S10_M_17",40,500.0,4000.0);
  // Content
  S10_M_17->SetBinContent(0,0.0); // underflow
  S10_M_17->SetBinContent(1,12.239368935);
  S10_M_17->SetBinContent(2,9.08260974103);
  S10_M_17->SetBinContent(3,6.61203027319);
  S10_M_17->SetBinContent(4,4.89685575338);
  S10_M_17->SetBinContent(5,3.41533988202);
  S10_M_17->SetBinContent(6,2.34079576656);
  S10_M_17->SetBinContent(7,2.01902785968);
  S10_M_17->SetBinContent(8,1.67520583345);
  S10_M_17->SetBinContent(9,0.944491242049);
  S10_M_17->SetBinContent(10,0.94514280354);
  S10_M_17->SetBinContent(11,0.493499871795);
  S10_M_17->SetBinContent(12,0.536815064947);
  S10_M_17->SetBinContent(13,0.429522906458);
  S10_M_17->SetBinContent(14,0.257739356465);
  S10_M_17->SetBinContent(15,0.171821638974);
  S10_M_17->SetBinContent(16,0.150352125482);
  S10_M_17->SetBinContent(17,0.0857590633925);
  S10_M_17->SetBinContent(18,0.128961264235);
  S10_M_17->SetBinContent(19,0.0643875915357);
  S10_M_17->SetBinContent(20,0.0426650487499);
  S10_M_17->SetBinContent(21,0.107311427914);
  S10_M_17->SetBinContent(22,0.0426027342786);
  S10_M_17->SetBinContent(23,0.0);
  S10_M_17->SetBinContent(24,0.0);
  S10_M_17->SetBinContent(25,0.0);
  S10_M_17->SetBinContent(26,0.0427797880538);
  S10_M_17->SetBinContent(27,0.0);
  S10_M_17->SetBinContent(28,0.0);
  S10_M_17->SetBinContent(29,0.0);
  S10_M_17->SetBinContent(30,0.0);
  S10_M_17->SetBinContent(31,0.0);
  S10_M_17->SetBinContent(32,0.0);
  S10_M_17->SetBinContent(33,0.0);
  S10_M_17->SetBinContent(34,0.0);
  S10_M_17->SetBinContent(35,0.0);
  S10_M_17->SetBinContent(36,0.0);
  S10_M_17->SetBinContent(37,0.0);
  S10_M_17->SetBinContent(38,0.0);
  S10_M_17->SetBinContent(39,0.0);
  S10_M_17->SetBinContent(40,0.0);
  S10_M_17->SetBinContent(41,0.0); // overflow
  S10_M_17->SetEntries(2176);
  // Style
  S10_M_17->SetLineColor(18);
  S10_M_17->SetLineStyle(1);
  S10_M_17->SetLineWidth(1);
  S10_M_17->SetFillColor(0);
  S10_M_17->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S10_M_18 = new TH1F("S10_M_18","S10_M_18",40,500.0,4000.0);
  // Content
  S10_M_18->SetBinContent(0,0.0); // underflow
  S10_M_18->SetBinContent(1,1.04779044477);
  S10_M_18->SetBinContent(2,0.779111479224);
  S10_M_18->SetBinContent(3,0.521424025918);
  S10_M_18->SetBinContent(4,0.401587027723);
  S10_M_18->SetBinContent(5,0.270571401637);
  S10_M_18->SetBinContent(6,0.236365132845);
  S10_M_18->SetBinContent(7,0.197527555215);
  S10_M_18->SetBinContent(8,0.150412569549);
  S10_M_18->SetBinContent(9,0.105289942815);
  S10_M_18->SetBinContent(10,0.0940056714331);
  S10_M_18->SetBinContent(11,0.0583188221486);
  S10_M_18->SetBinContent(12,0.0680496218575);
  S10_M_18->SetBinContent(13,0.0372721931684);
  S10_M_18->SetBinContent(14,0.0437476583011);
  S10_M_18->SetBinContent(15,0.0194314025412);
  S10_M_18->SetBinContent(16,0.0226730138362);
  S10_M_18->SetBinContent(17,0.0113404500826);
  S10_M_18->SetBinContent(18,0.0129620792527);
  S10_M_18->SetBinContent(19,0.00810970174238);
  S10_M_18->SetBinContent(20,0.00324519141805);
  S10_M_18->SetBinContent(21,0.00323792744573);
  S10_M_18->SetBinContent(22,0.00486698717858);
  S10_M_18->SetBinContent(23,0.00162106527712);
  S10_M_18->SetBinContent(24,0.00485074932442);
  S10_M_18->SetBinContent(25,0.00162219023415);
  S10_M_18->SetBinContent(26,0.00324236881003);
  S10_M_18->SetBinContent(27,0.0);
  S10_M_18->SetBinContent(28,0.00161444629275);
  S10_M_18->SetBinContent(29,0.0);
  S10_M_18->SetBinContent(30,0.00323712906885);
  S10_M_18->SetBinContent(31,0.00161870660779);
  S10_M_18->SetBinContent(32,0.0);
  S10_M_18->SetBinContent(33,0.0);
  S10_M_18->SetBinContent(34,0.0);
  S10_M_18->SetBinContent(35,0.0);
  S10_M_18->SetBinContent(36,0.0);
  S10_M_18->SetBinContent(37,0.0);
  S10_M_18->SetBinContent(38,0.00161842371835);
  S10_M_18->SetBinContent(39,0.0);
  S10_M_18->SetBinContent(40,0.0);
  S10_M_18->SetBinContent(41,0.0); // overflow
  S10_M_18->SetEntries(2542);
  // Style
  S10_M_18->SetLineColor(19);
  S10_M_18->SetLineStyle(1);
  S10_M_18->SetLineWidth(1);
  S10_M_18->SetFillColor(0);
  S10_M_18->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S10_M_19 = new TH1F("S10_M_19","S10_M_19",40,500.0,4000.0);
  // Content
  S10_M_19->SetBinContent(0,0.0); // underflow
  S10_M_19->SetBinContent(1,0.0829551828044);
  S10_M_19->SetBinContent(2,0.0553342510094);
  S10_M_19->SetBinContent(3,0.0614457300278);
  S10_M_19->SetBinContent(4,0.0638546406694);
  S10_M_19->SetBinContent(5,0.0255513801011);
  S10_M_19->SetBinContent(6,0.0403435792613);
  S10_M_19->SetBinContent(7,0.0105847050275);
  S10_M_19->SetBinContent(8,0.0255709355867);
  S10_M_19->SetBinContent(9,0.00425990862504);
  S10_M_19->SetBinContent(10,0.0170424052318);
  S10_M_19->SetBinContent(11,0.00851587719838);
  S10_M_19->SetBinContent(12,0.0127698657231);
  S10_M_19->SetBinContent(13,0.00213366829569);
  S10_M_19->SetBinContent(14,0.00426130512726);
  S10_M_19->SetBinContent(15,0.00213366829569);
  S10_M_19->SetBinContent(16,0.0);
  S10_M_19->SetBinContent(17,0.00635995618555);
  S10_M_19->SetBinContent(18,0.0);
  S10_M_19->SetBinContent(19,0.0063660644907);
  S10_M_19->SetBinContent(20,0.0);
  S10_M_19->SetBinContent(21,0.0);
  S10_M_19->SetBinContent(22,0.00213219495244);
  S10_M_19->SetBinContent(23,0.0);
  S10_M_19->SetBinContent(24,0.0);
  S10_M_19->SetBinContent(25,0.00212624032935);
  S10_M_19->SetBinContent(26,0.0);
  S10_M_19->SetBinContent(27,0.0);
  S10_M_19->SetBinContent(28,0.0);
  S10_M_19->SetBinContent(29,0.00212763683157);
  S10_M_19->SetBinContent(30,0.0);
  S10_M_19->SetBinContent(31,0.0);
  S10_M_19->SetBinContent(32,0.0);
  S10_M_19->SetBinContent(33,0.0);
  S10_M_19->SetBinContent(34,0.0);
  S10_M_19->SetBinContent(35,0.0);
  S10_M_19->SetBinContent(36,0.0);
  S10_M_19->SetBinContent(37,0.0);
  S10_M_19->SetBinContent(38,0.0);
  S10_M_19->SetBinContent(39,0.0);
  S10_M_19->SetBinContent(40,0.0);
  S10_M_19->SetBinContent(41,0.0); // overflow
  S10_M_19->SetEntries(205);
  // Style
  S10_M_19->SetLineColor(20);
  S10_M_19->SetLineStyle(1);
  S10_M_19->SetLineWidth(1);
  S10_M_19->SetFillColor(0);
  S10_M_19->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_20","mystack");
  stack->Add(S10_M_0);
  stack->Add(S10_M_1);
  stack->Add(S10_M_2);
  stack->Add(S10_M_3);
  stack->Add(S10_M_4);
  stack->Add(S10_M_5);
  stack->Add(S10_M_6);
  stack->Add(S10_M_7);
  stack->Add(S10_M_8);
  stack->Add(S10_M_9);
  stack->Add(S10_M_10);
  stack->Add(S10_M_11);
  stack->Add(S10_M_12);
  stack->Add(S10_M_13);
  stack->Add(S10_M_14);
  stack->Add(S10_M_15);
  stack->Add(S10_M_16);
  stack->Add(S10_M_17);
  stack->Add(S10_M_18);
  stack->Add(S10_M_19);
  stack->Draw("");

  // Y axis
  stack->GetYaxis()->SetLabelSize(0.04);
  stack->GetYaxis()->SetLabelOffset(0.005);
  stack->GetYaxis()->SetTitleSize(0.04);
  stack->GetYaxis()->SetTitleFont(22);
  stack->GetYaxis()->SetTitleOffset(1);
  stack->GetYaxis()->SetTitle("Events  ( L_{int} = 3000.0 fb^{-1} )");

  // X axis
  stack->GetXaxis()->SetLabelSize(0.04);
  stack->GetXaxis()->SetLabelOffset(0.005);
  stack->GetXaxis()->SetTitleSize(0.06);
  stack->GetXaxis()->SetTitleFont(22);
  stack->GetXaxis()->SetTitleOffset(1);
  stack->GetXaxis()->SetTitle("M [ a_{1} , a_{2} ]   ( GeV ) ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(0);

  // Creating a TLegend
  TLegend* legend = new TLegend(.73,.5,.97,.95);
  legend->AddEntry(S10_M_0,"signal_1pt8TeVL");
  legend->AddEntry(S10_M_1,"signal_2TeVL");
  legend->AddEntry(S10_M_2,"signal_2pt2TeVL");
  legend->AddEntry(S10_M_3,"signal_2pt4TeVL");
  legend->AddEntry(S10_M_4,"bg_dip_0_100");
  legend->AddEntry(S10_M_5,"bg_dip_100_200");
  legend->AddEntry(S10_M_6,"bg_dip_200_400");
  legend->AddEntry(S10_M_7,"bg_dip_400_600");
  legend->AddEntry(S10_M_8,"bg_dip_600_800");
  legend->AddEntry(S10_M_9,"bg_dip_800_1200");
  legend->AddEntry(S10_M_10,"bg_dip_1200_1600");
  legend->AddEntry(S10_M_11,"bg_dip_1600_inf");
  legend->AddEntry(S10_M_12,"bg_vbf_0_100");
  legend->AddEntry(S10_M_13,"bg_vbf_100_200");
  legend->AddEntry(S10_M_14,"bg_vbf_200_400");
  legend->AddEntry(S10_M_15,"bg_vbf_400_600");
  legend->AddEntry(S10_M_16,"bg_vbf_600_800");
  legend->AddEntry(S10_M_17,"bg_vbf_800_1200");
  legend->AddEntry(S10_M_18,"bg_vbf_1200_1600");
  legend->AddEntry(S10_M_19,"bg_vbf_1600_inf");
  legend->SetFillColor(0);
  legend->SetTextSize(0.05);
  legend->SetTextFont(22);
  legend->SetY1(TMath::Max(0.15,0.97-0.10*legend->GetListOfPrimitives()->GetSize()));
  legend->Draw();

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_9.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_9.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_9.eps");

}
