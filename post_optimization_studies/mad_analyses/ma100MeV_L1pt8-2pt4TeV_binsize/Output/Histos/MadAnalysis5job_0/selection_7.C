void selection_7()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo15","canvas_plotflow_tempo15",0,0,1000,500);
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
  TH1F* S8_M_0 = new TH1F("S8_M_0","S8_M_0",20,750.0,6000.0);
  // Content
  S8_M_0->SetBinContent(0,0.0); // underflow
  S8_M_0->SetBinContent(1,556.846139685);
  S8_M_0->SetBinContent(2,576.217137587);
  S8_M_0->SetBinContent(3,525.13644312);
  S8_M_0->SetBinContent(4,448.714151398);
  S8_M_0->SetBinContent(5,382.242858598);
  S8_M_0->SetBinContent(6,292.420528327);
  S8_M_0->SetBinContent(7,224.62248567);
  S8_M_0->SetBinContent(8,168.234671778);
  S8_M_0->SetBinContent(9,125.645296391);
  S8_M_0->SetBinContent(10,96.1909695811);
  S8_M_0->SetBinContent(11,65.6752128864);
  S8_M_0->SetBinContent(12,45.2429350995);
  S8_M_0->SetBinContent(13,32.7712764504);
  S8_M_0->SetBinContent(14,20.03425583);
  S8_M_0->SetBinContent(15,12.2063026779);
  S8_M_0->SetBinContent(16,9.95078892218);
  S8_M_0->SetBinContent(17,8.49134008026);
  S8_M_0->SetBinContent(18,3.98031556887);
  S8_M_0->SetBinContent(19,4.37834652576);
  S8_M_0->SetBinContent(20,1.19409467066);
  S8_M_0->SetBinContent(21,2.91889798384); // overflow
  S8_M_0->SetEntries(27157);
  // Style
  S8_M_0->SetLineColor(1);
  S8_M_0->SetLineStyle(1);
  S8_M_0->SetLineWidth(1);
  S8_M_0->SetFillColor(0);
  S8_M_0->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S8_M_1 = new TH1F("S8_M_1","S8_M_1",20,750.0,6000.0);
  // Content
  S8_M_1->SetBinContent(0,0.0); // underflow
  S8_M_1->SetBinContent(1,345.736664738);
  S8_M_1->SetBinContent(2,368.333895064);
  S8_M_1->SetBinContent(3,336.04207403);
  S8_M_1->SetBinContent(4,314.245207243);
  S8_M_1->SetBinContent(5,240.19380409);
  S8_M_1->SetBinContent(6,195.385796126);
  S8_M_1->SetBinContent(7,148.988961622);
  S8_M_1->SetBinContent(8,112.520292085);
  S8_M_1->SetBinContent(9,83.7509399285);
  S8_M_1->SetBinContent(10,59.3886532041);
  S8_M_1->SetBinContent(11,42.2331755112);
  S8_M_1->SetBinContent(12,30.6136055769);
  S8_M_1->SetBinContent(13,20.9147282774);
  S8_M_1->SetBinContent(14,14.2651671136);
  S8_M_1->SetBinContent(15,8.97627492427);
  S8_M_1->SetBinContent(16,7.29258282285);
  S8_M_1->SetBinContent(17,3.68689712112);
  S8_M_1->SetBinContent(18,2.88425299642);
  S8_M_1->SetBinContent(19,1.92352837982);
  S8_M_1->SetBinContent(20,1.52245691819);
  S8_M_1->SetBinContent(21,2.88534622707); // overflow
  S8_M_1->SetEntries(29220);
  // Style
  S8_M_1->SetLineColor(2);
  S8_M_1->SetLineStyle(1);
  S8_M_1->SetLineWidth(1);
  S8_M_1->SetFillColor(0);
  S8_M_1->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S8_M_2 = new TH1F("S8_M_2","S8_M_2",20,750.0,6000.0);
  // Content
  S8_M_2->SetBinContent(0,0.0); // underflow
  S8_M_2->SetBinContent(1,232.818536368);
  S8_M_2->SetBinContent(2,242.818768789);
  S8_M_2->SetBinContent(3,236.516547264);
  S8_M_2->SetBinContent(4,206.255329937);
  S8_M_2->SetBinContent(5,166.150120227);
  S8_M_2->SetBinContent(6,128.597071135);
  S8_M_2->SetBinContent(7,103.596415082);
  S8_M_2->SetBinContent(8,76.2519784615);
  S8_M_2->SetBinContent(9,56.5118836822);
  S8_M_2->SetBinContent(10,42.9698504035);
  S8_M_2->SetBinContent(11,29.011168024);
  S8_M_2->SetBinContent(12,20.1567708802);
  S8_M_2->SetBinContent(13,15.2087256822);
  S8_M_2->SetBinContent(14,10.2606834842);
  S8_M_2->SetBinContent(15,7.08351771501);
  S8_M_2->SetBinContent(16,4.73970714754);
  S8_M_2->SetBinContent(17,2.96882681879);
  S8_M_2->SetBinContent(18,1.61462499092);
  S8_M_2->SetBinContent(19,1.35420182787);
  S8_M_2->SetBinContent(20,0.781270089155);
  S8_M_2->SetBinContent(21,1.61462499092); // overflow
  S8_M_2->SetEntries(30475);
  // Style
  S8_M_2->SetLineColor(3);
  S8_M_2->SetLineStyle(1);
  S8_M_2->SetLineWidth(1);
  S8_M_2->SetFillColor(0);
  S8_M_2->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S8_M_3 = new TH1F("S8_M_3","S8_M_3",20,750.0,6000.0);
  // Content
  S8_M_3->SetBinContent(0,0.0); // underflow
  S8_M_3->SetBinContent(1,169.77140219);
  S8_M_3->SetBinContent(2,175.49684395);
  S8_M_3->SetBinContent(3,165.432890856);
  S8_M_3->SetBinContent(4,137.659212318);
  S8_M_3->SetBinContent(5,114.473015191);
  S8_M_3->SetBinContent(6,91.9269282597);
  S8_M_3->SetBinContent(7,71.0166518316);
  S8_M_3->SetBinContent(8,52.417906114);
  S8_M_3->SetBinContent(9,39.6157021784);
  S8_M_3->SetBinContent(10,29.907366194);
  S8_M_3->SetBinContent(11,20.5190853079);
  S8_M_3->SetBinContent(12,14.0112973073);
  S8_M_3->SetBinContent(13,10.4195702031);
  S8_M_3->SetBinContent(14,7.2901432411);
  S8_M_3->SetBinContent(15,4.69414044305);
  S8_M_3->SetBinContent(16,3.0938649511);
  S8_M_3->SetBinContent(17,1.92033029034);
  S8_M_3->SetBinContent(18,1.74252173568);
  S8_M_3->SetBinContent(19,0.568986774915);
  S8_M_3->SetBinContent(20,0.746795029576);
  S8_M_3->SetBinContent(21,0.462301642118); // overflow
  S8_M_3->SetEntries(31303);
  // Style
  S8_M_3->SetLineColor(4);
  S8_M_3->SetLineStyle(1);
  S8_M_3->SetLineWidth(1);
  S8_M_3->SetFillColor(0);
  S8_M_3->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S8_M_4 = new TH1F("S8_M_4","S8_M_4",20,750.0,6000.0);
  // Content
  S8_M_4->SetBinContent(0,0.0); // underflow
  S8_M_4->SetBinContent(1,0.0);
  S8_M_4->SetBinContent(2,0.0);
  S8_M_4->SetBinContent(3,0.0);
  S8_M_4->SetBinContent(4,0.0);
  S8_M_4->SetBinContent(5,0.0);
  S8_M_4->SetBinContent(6,0.0);
  S8_M_4->SetBinContent(7,0.0);
  S8_M_4->SetBinContent(8,0.0);
  S8_M_4->SetBinContent(9,0.0);
  S8_M_4->SetBinContent(10,0.0);
  S8_M_4->SetBinContent(11,0.0);
  S8_M_4->SetBinContent(12,0.0);
  S8_M_4->SetBinContent(13,0.0);
  S8_M_4->SetBinContent(14,0.0);
  S8_M_4->SetBinContent(15,0.0);
  S8_M_4->SetBinContent(16,0.0);
  S8_M_4->SetBinContent(17,0.0);
  S8_M_4->SetBinContent(18,0.0);
  S8_M_4->SetBinContent(19,0.0);
  S8_M_4->SetBinContent(20,0.0);
  S8_M_4->SetBinContent(21,0.0); // overflow
  S8_M_4->SetEntries(0);
  // Style
  S8_M_4->SetLineColor(5);
  S8_M_4->SetLineStyle(1);
  S8_M_4->SetLineWidth(1);
  S8_M_4->SetFillColor(0);
  S8_M_4->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S8_M_5 = new TH1F("S8_M_5","S8_M_5",20,750.0,6000.0);
  // Content
  S8_M_5->SetBinContent(0,0.0); // underflow
  S8_M_5->SetBinContent(1,0.0);
  S8_M_5->SetBinContent(2,157.880409317);
  S8_M_5->SetBinContent(3,79.0971195289);
  S8_M_5->SetBinContent(4,0.0);
  S8_M_5->SetBinContent(5,0.0);
  S8_M_5->SetBinContent(6,0.0);
  S8_M_5->SetBinContent(7,0.0);
  S8_M_5->SetBinContent(8,0.0);
  S8_M_5->SetBinContent(9,0.0);
  S8_M_5->SetBinContent(10,0.0);
  S8_M_5->SetBinContent(11,0.0);
  S8_M_5->SetBinContent(12,0.0);
  S8_M_5->SetBinContent(13,0.0);
  S8_M_5->SetBinContent(14,0.0);
  S8_M_5->SetBinContent(15,0.0);
  S8_M_5->SetBinContent(16,0.0);
  S8_M_5->SetBinContent(17,0.0);
  S8_M_5->SetBinContent(18,0.0);
  S8_M_5->SetBinContent(19,0.0);
  S8_M_5->SetBinContent(20,0.0);
  S8_M_5->SetBinContent(21,0.0); // overflow
  S8_M_5->SetEntries(3);
  // Style
  S8_M_5->SetLineColor(6);
  S8_M_5->SetLineStyle(1);
  S8_M_5->SetLineWidth(1);
  S8_M_5->SetFillColor(0);
  S8_M_5->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S8_M_6 = new TH1F("S8_M_6","S8_M_6",20,750.0,6000.0);
  // Content
  S8_M_6->SetBinContent(0,0.0); // underflow
  S8_M_6->SetBinContent(1,587.379391599);
  S8_M_6->SetBinContent(2,431.646019427);
  S8_M_6->SetBinContent(3,241.972483967);
  S8_M_6->SetBinContent(4,69.1428839324);
  S8_M_6->SetBinContent(5,51.7944212727);
  S8_M_6->SetBinContent(6,34.5899157442);
  S8_M_6->SetBinContent(7,17.3128927115);
  S8_M_6->SetBinContent(8,0.0);
  S8_M_6->SetBinContent(9,0.0);
  S8_M_6->SetBinContent(10,0.0);
  S8_M_6->SetBinContent(11,0.0);
  S8_M_6->SetBinContent(12,0.0);
  S8_M_6->SetBinContent(13,0.0);
  S8_M_6->SetBinContent(14,0.0);
  S8_M_6->SetBinContent(15,0.0);
  S8_M_6->SetBinContent(16,0.0);
  S8_M_6->SetBinContent(17,0.0);
  S8_M_6->SetBinContent(18,0.0);
  S8_M_6->SetBinContent(19,0.0);
  S8_M_6->SetBinContent(20,0.0);
  S8_M_6->SetBinContent(21,0.0); // overflow
  S8_M_6->SetEntries(83);
  // Style
  S8_M_6->SetLineColor(7);
  S8_M_6->SetLineStyle(1);
  S8_M_6->SetLineWidth(1);
  S8_M_6->SetFillColor(0);
  S8_M_6->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S8_M_7 = new TH1F("S8_M_7","S8_M_7",20,750.0,6000.0);
  // Content
  S8_M_7->SetBinContent(0,0.0); // underflow
  S8_M_7->SetBinContent(1,222.253013534);
  S8_M_7->SetBinContent(2,236.78229385);
  S8_M_7->SetBinContent(3,197.272667187);
  S8_M_7->SetBinContent(4,101.752854311);
  S8_M_7->SetBinContent(5,74.7652519532);
  S8_M_7->SetBinContent(6,49.8410778464);
  S8_M_7->SetBinContent(7,22.8325356777);
  S8_M_7->SetBinContent(8,2.07793955731);
  S8_M_7->SetBinContent(9,8.30798975567);
  S8_M_7->SetBinContent(10,4.14912921356);
  S8_M_7->SetBinContent(11,0.0);
  S8_M_7->SetBinContent(12,0.0);
  S8_M_7->SetBinContent(13,0.0);
  S8_M_7->SetBinContent(14,0.0);
  S8_M_7->SetBinContent(15,0.0);
  S8_M_7->SetBinContent(16,0.0);
  S8_M_7->SetBinContent(17,0.0);
  S8_M_7->SetBinContent(18,0.0);
  S8_M_7->SetBinContent(19,0.0);
  S8_M_7->SetBinContent(20,0.0);
  S8_M_7->SetBinContent(21,0.0); // overflow
  S8_M_7->SetEntries(443);
  // Style
  S8_M_7->SetLineColor(8);
  S8_M_7->SetLineStyle(1);
  S8_M_7->SetLineWidth(1);
  S8_M_7->SetFillColor(0);
  S8_M_7->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S8_M_8 = new TH1F("S8_M_8","S8_M_8",20,750.0,6000.0);
  // Content
  S8_M_8->SetBinContent(0,0.0); // underflow
  S8_M_8->SetBinContent(1,36.3056646945);
  S8_M_8->SetBinContent(2,44.6289815042);
  S8_M_8->SetBinContent(3,43.8471908417);
  S8_M_8->SetBinContent(4,32.5124870417);
  S8_M_8->SetBinContent(5,38.562293246);
  S8_M_8->SetBinContent(6,30.2483983429);
  S8_M_8->SetBinContent(7,22.6859073156);
  S8_M_8->SetBinContent(8,9.0634417076);
  S8_M_8->SetBinContent(9,5.29110148876);
  S8_M_8->SetBinContent(10,3.0236950954);
  S8_M_8->SetBinContent(11,0.753221803182);
  S8_M_8->SetBinContent(12,0.75534287007);
  S8_M_8->SetBinContent(13,2.26722796885);
  S8_M_8->SetBinContent(14,0.0);
  S8_M_8->SetBinContent(15,0.0);
  S8_M_8->SetBinContent(16,0.0);
  S8_M_8->SetBinContent(17,0.0);
  S8_M_8->SetBinContent(18,0.0);
  S8_M_8->SetBinContent(19,0.0);
  S8_M_8->SetBinContent(20,0.0);
  S8_M_8->SetBinContent(21,0.0); // overflow
  S8_M_8->SetEntries(357);
  // Style
  S8_M_8->SetLineColor(9);
  S8_M_8->SetLineStyle(1);
  S8_M_8->SetLineWidth(1);
  S8_M_8->SetFillColor(0);
  S8_M_8->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S8_M_9 = new TH1F("S8_M_9","S8_M_9",20,750.0,6000.0);
  // Content
  S8_M_9->SetBinContent(0,0.0); // underflow
  S8_M_9->SetBinContent(1,6.153787524);
  S8_M_9->SetBinContent(2,15.7051307614);
  S8_M_9->SetBinContent(3,15.4887783389);
  S8_M_9->SetBinContent(4,12.5204330284);
  S8_M_9->SetBinContent(5,9.96863329331);
  S8_M_9->SetBinContent(6,9.33512643731);
  S8_M_9->SetBinContent(7,10.1866910959);
  S8_M_9->SetBinContent(8,9.12420179807);
  S8_M_9->SetBinContent(9,6.15119626968);
  S8_M_9->SetBinContent(10,5.51939479375);
  S8_M_9->SetBinContent(11,4.03053162194);
  S8_M_9->SetBinContent(12,2.54574635727);
  S8_M_9->SetBinContent(13,1.06101361022);
  S8_M_9->SetBinContent(14,1.48555946683);
  S8_M_9->SetBinContent(15,0.212260578002);
  S8_M_9->SetBinContent(16,0.212031289507);
  S8_M_9->SetBinContent(17,0.0);
  S8_M_9->SetBinContent(18,0.212281036791);
  S8_M_9->SetBinContent(19,0.0);
  S8_M_9->SetBinContent(20,0.424877698747);
  S8_M_9->SetBinContent(21,0.0); // overflow
  S8_M_9->SetEntries(520);
  // Style
  S8_M_9->SetLineColor(10);
  S8_M_9->SetLineStyle(1);
  S8_M_9->SetLineWidth(1);
  S8_M_9->SetFillColor(0);
  S8_M_9->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S8_M_10 = new TH1F("S8_M_10","S8_M_10",20,750.0,6000.0);
  // Content
  S8_M_10->SetBinContent(0,0.0); // underflow
  S8_M_10->SetBinContent(1,0.0);
  S8_M_10->SetBinContent(2,0.342229130968);
  S8_M_10->SetBinContent(3,0.910578099182);
  S8_M_10->SetBinContent(4,1.02754571386);
  S8_M_10->SetBinContent(5,1.02942758454);
  S8_M_10->SetBinContent(6,0.798495104572);
  S8_M_10->SetBinContent(7,0.800384243903);
  S8_M_10->SetBinContent(8,0.229144835782);
  S8_M_10->SetBinContent(9,0.113137214489);
  S8_M_10->SetBinContent(10,0.0);
  S8_M_10->SetBinContent(11,0.45840375388);
  S8_M_10->SetBinContent(12,0.457575393939);
  S8_M_10->SetBinContent(13,0.115000204415);
  S8_M_10->SetBinContent(14,0.57050970678);
  S8_M_10->SetBinContent(15,0.572815641021);
  S8_M_10->SetBinContent(16,0.113137214489);
  S8_M_10->SetBinContent(17,0.115000204415);
  S8_M_10->SetBinContent(18,0.0);
  S8_M_10->SetBinContent(19,0.114144631366);
  S8_M_10->SetBinContent(20,0.115222164104);
  S8_M_10->SetBinContent(21,0.0); // overflow
  S8_M_10->SetEntries(69);
  // Style
  S8_M_10->SetLineColor(11);
  S8_M_10->SetLineStyle(1);
  S8_M_10->SetLineWidth(1);
  S8_M_10->SetFillColor(0);
  S8_M_10->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S8_M_11 = new TH1F("S8_M_11","S8_M_11",20,750.0,6000.0);
  // Content
  S8_M_11->SetBinContent(0,0.0); // underflow
  S8_M_11->SetBinContent(1,0.0);
  S8_M_11->SetBinContent(2,0.0271125965826);
  S8_M_11->SetBinContent(3,0.0677184454599);
  S8_M_11->SetBinContent(4,0.0947422665806);
  S8_M_11->SetBinContent(5,0.0947957120304);
  S8_M_11->SetBinContent(6,0.0948460679809);
  S8_M_11->SetBinContent(7,0.0812186332474);
  S8_M_11->SetBinContent(8,0.027096664006);
  S8_M_11->SetBinContent(9,0.0406829015663);
  S8_M_11->SetBinContent(10,0.0270118644699);
  S8_M_11->SetBinContent(11,0.0135575225415);
  S8_M_11->SetBinContent(12,0.0135469604963);
  S8_M_11->SetBinContent(13,0.0271029209639);
  S8_M_11->SetBinContent(14,0.0);
  S8_M_11->SetBinContent(15,0.0406195812684);
  S8_M_11->SetBinContent(16,0.0);
  S8_M_11->SetBinContent(17,0.0135469604963);
  S8_M_11->SetBinContent(18,0.0270792299906);
  S8_M_11->SetBinContent(19,0.0135002715216);
  S8_M_11->SetBinContent(20,0.0270939181053);
  S8_M_11->SetBinContent(21,0.0); // overflow
  S8_M_11->SetEntries(54);
  // Style
  S8_M_11->SetLineColor(12);
  S8_M_11->SetLineStyle(1);
  S8_M_11->SetLineWidth(1);
  S8_M_11->SetFillColor(0);
  S8_M_11->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S8_M_12 = new TH1F("S8_M_12","S8_M_12",20,750.0,6000.0);
  // Content
  S8_M_12->SetBinContent(0,0.0); // underflow
  S8_M_12->SetBinContent(1,2.73194704997);
  S8_M_12->SetBinContent(2,0.913150150035);
  S8_M_12->SetBinContent(3,0.0);
  S8_M_12->SetBinContent(4,0.0);
  S8_M_12->SetBinContent(5,0.0);
  S8_M_12->SetBinContent(6,0.0);
  S8_M_12->SetBinContent(7,0.0);
  S8_M_12->SetBinContent(8,0.0);
  S8_M_12->SetBinContent(9,0.0);
  S8_M_12->SetBinContent(10,0.0);
  S8_M_12->SetBinContent(11,0.0);
  S8_M_12->SetBinContent(12,0.0);
  S8_M_12->SetBinContent(13,0.0);
  S8_M_12->SetBinContent(14,0.0);
  S8_M_12->SetBinContent(15,0.0);
  S8_M_12->SetBinContent(16,0.0);
  S8_M_12->SetBinContent(17,0.0);
  S8_M_12->SetBinContent(18,0.0);
  S8_M_12->SetBinContent(19,0.0);
  S8_M_12->SetBinContent(20,0.0);
  S8_M_12->SetBinContent(21,0.0); // overflow
  S8_M_12->SetEntries(4);
  // Style
  S8_M_12->SetLineColor(13);
  S8_M_12->SetLineStyle(1);
  S8_M_12->SetLineWidth(1);
  S8_M_12->SetFillColor(0);
  S8_M_12->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S8_M_13 = new TH1F("S8_M_13","S8_M_13",20,750.0,6000.0);
  // Content
  S8_M_13->SetBinContent(0,0.0); // underflow
  S8_M_13->SetBinContent(1,25.5997769691);
  S8_M_13->SetBinContent(2,19.5787601161);
  S8_M_13->SetBinContent(3,18.0732649535);
  S8_M_13->SetBinContent(4,4.52159578422);
  S8_M_13->SetBinContent(5,7.52873711732);
  S8_M_13->SetBinContent(6,6.02253847545);
  S8_M_13->SetBinContent(7,3.76406330445);
  S8_M_13->SetBinContent(8,0.752556991122);
  S8_M_13->SetBinContent(9,0.0);
  S8_M_13->SetBinContent(10,0.754386037151);
  S8_M_13->SetBinContent(11,0.0);
  S8_M_13->SetBinContent(12,0.753054694938);
  S8_M_13->SetBinContent(13,0.0);
  S8_M_13->SetBinContent(14,0.0);
  S8_M_13->SetBinContent(15,0.0);
  S8_M_13->SetBinContent(16,0.0);
  S8_M_13->SetBinContent(17,0.0);
  S8_M_13->SetBinContent(18,0.0);
  S8_M_13->SetBinContent(19,0.0);
  S8_M_13->SetBinContent(20,0.0);
  S8_M_13->SetBinContent(21,0.0); // overflow
  S8_M_13->SetEntries(116);
  // Style
  S8_M_13->SetLineColor(14);
  S8_M_13->SetLineStyle(1);
  S8_M_13->SetLineWidth(1);
  S8_M_13->SetFillColor(0);
  S8_M_13->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S8_M_14 = new TH1F("S8_M_14","S8_M_14",20,750.0,6000.0);
  // Content
  S8_M_14->SetBinContent(0,0.0); // underflow
  S8_M_14->SetBinContent(1,77.9670856012);
  S8_M_14->SetBinContent(2,92.8067768048);
  S8_M_14->SetBinContent(3,74.6868184437);
  S8_M_14->SetBinContent(4,60.6289093159);
  S8_M_14->SetBinContent(5,32.5934691537);
  S8_M_14->SetBinContent(6,35.4779092418);
  S8_M_14->SetBinContent(7,23.1072453713);
  S8_M_14->SetBinContent(8,16.0895370372);
  S8_M_14->SetBinContent(9,13.1999841955);
  S8_M_14->SetBinContent(10,5.36290986665);
  S8_M_14->SetBinContent(11,9.0681083979);
  S8_M_14->SetBinContent(12,3.7129803982);
  S8_M_14->SetBinContent(13,1.23649386834);
  S8_M_14->SetBinContent(14,2.06385227314);
  S8_M_14->SetBinContent(15,1.23831105919);
  S8_M_14->SetBinContent(16,2.06414569279);
  S8_M_14->SetBinContent(17,1.64965585386);
  S8_M_14->SetBinContent(18,0.0);
  S8_M_14->SetBinContent(19,0.413164727762);
  S8_M_14->SetBinContent(20,0.0);
  S8_M_14->SetBinContent(21,0.0); // overflow
  S8_M_14->SetEntries(1099);
  // Style
  S8_M_14->SetLineColor(15);
  S8_M_14->SetLineStyle(1);
  S8_M_14->SetLineWidth(1);
  S8_M_14->SetFillColor(0);
  S8_M_14->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S8_M_15 = new TH1F("S8_M_15","S8_M_15",20,750.0,6000.0);
  // Content
  S8_M_15->SetBinContent(0,0.0); // underflow
  S8_M_15->SetBinContent(1,11.9137375642);
  S8_M_15->SetBinContent(2,30.4178365241);
  S8_M_15->SetBinContent(3,50.9931679587);
  S8_M_15->SetBinContent(4,57.28857737);
  S8_M_15->SetBinContent(5,48.7037833278);
  S8_M_15->SetBinContent(6,35.3023380648);
  S8_M_15->SetBinContent(7,26.5686611208);
  S8_M_15->SetBinContent(8,20.2084436814);
  S8_M_15->SetBinContent(9,15.249033223);
  S8_M_15->SetBinContent(10,10.8063704403);
  S8_M_15->SetBinContent(11,7.7723488404);
  S8_M_15->SetBinContent(12,4.95864687921);
  S8_M_15->SetBinContent(13,4.14520962577);
  S8_M_15->SetBinContent(14,3.10857277768);
  S8_M_15->SetBinContent(15,1.48034156501);
  S8_M_15->SetBinContent(16,1.48004605387);
  S8_M_15->SetBinContent(17,0.444294536715);
  S8_M_15->SetBinContent(18,0.740638399577);
  S8_M_15->SetBinContent(19,0.517983531463);
  S8_M_15->SetBinContent(20,0.517808269006);
  S8_M_15->SetBinContent(21,0.147845366068); // overflow
  S8_M_15->SetEntries(4496);
  // Style
  S8_M_15->SetLineColor(16);
  S8_M_15->SetLineStyle(1);
  S8_M_15->SetLineWidth(1);
  S8_M_15->SetFillColor(0);
  S8_M_15->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S8_M_16 = new TH1F("S8_M_16","S8_M_16",20,750.0,6000.0);
  // Content
  S8_M_16->SetBinContent(0,0.0); // underflow
  S8_M_16->SetBinContent(1,1.02110728423);
  S8_M_16->SetBinContent(2,3.45995273238);
  S8_M_16->SetBinContent(3,6.7875353267);
  S8_M_16->SetBinContent(4,10.6063377388);
  S8_M_16->SetBinContent(5,17.7901072339);
  S8_M_16->SetBinContent(6,19.8130497953);
  S8_M_16->SetBinContent(7,17.8277017815);
  S8_M_16->SetBinContent(8,12.4587274495);
  S8_M_16->SetBinContent(9,9.3399044253);
  S8_M_16->SetBinContent(10,6.73006320218);
  S8_M_16->SetBinContent(11,5.14196964296);
  S8_M_16->SetBinContent(12,3.87650260058);
  S8_M_16->SetBinContent(13,2.45774264999);
  S8_M_16->SetBinContent(14,1.83416739827);
  S8_M_16->SetBinContent(15,1.28541663948);
  S8_M_16->SetBinContent(16,0.850616550958);
  S8_M_16->SetBinContent(17,0.642643801639);
  S8_M_16->SetBinContent(18,0.453637273528);
  S8_M_16->SetBinContent(19,0.132301808903);
  S8_M_16->SetBinContent(20,0.189077948149);
  S8_M_16->SetBinContent(21,0.283522605762); // overflow
  S8_M_16->SetEntries(6505);
  // Style
  S8_M_16->SetLineColor(17);
  S8_M_16->SetLineStyle(1);
  S8_M_16->SetLineWidth(1);
  S8_M_16->SetFillColor(0);
  S8_M_16->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S8_M_17 = new TH1F("S8_M_17","S8_M_17",20,750.0,6000.0);
  // Content
  S8_M_17->SetBinContent(0,0.0); // underflow
  S8_M_17->SetBinContent(1,0.235964962811);
  S8_M_17->SetBinContent(2,0.579678918552);
  S8_M_17->SetBinContent(3,1.09528228028);
  S8_M_17->SetBinContent(4,1.87012754358);
  S8_M_17->SetBinContent(5,3.19908569912);
  S8_M_17->SetBinContent(6,4.27227412326);
  S8_M_17->SetBinContent(7,5.38970274449);
  S8_M_17->SetBinContent(8,5.453772453);
  S8_M_17->SetBinContent(9,5.47725190816);
  S8_M_17->SetBinContent(10,4.74604551597);
  S8_M_17->SetBinContent(11,4.14229848762);
  S8_M_17->SetBinContent(12,2.96213927034);
  S8_M_17->SetBinContent(13,2.1270571893);
  S8_M_17->SetBinContent(14,1.97546605909);
  S8_M_17->SetBinContent(15,1.05239844067);
  S8_M_17->SetBinContent(16,0.686671230462);
  S8_M_17->SetBinContent(17,0.558409298883);
  S8_M_17->SetBinContent(18,0.385908144934);
  S8_M_17->SetBinContent(19,0.171853341423);
  S8_M_17->SetBinContent(20,0.129089242159);
  S8_M_17->SetBinContent(21,0.214609118095); // overflow
  S8_M_17->SetEntries(2176);
  // Style
  S8_M_17->SetLineColor(18);
  S8_M_17->SetLineStyle(1);
  S8_M_17->SetLineWidth(1);
  S8_M_17->SetFillColor(0);
  S8_M_17->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S8_M_18 = new TH1F("S8_M_18","S8_M_18",20,750.0,6000.0);
  // Content
  S8_M_18->SetBinContent(0,0.0); // underflow
  S8_M_18->SetBinContent(1,0.00162106522106);
  S8_M_18->SetBinContent(2,0.0307919555687);
  S8_M_18->SetBinContent(3,0.0583229691766);
  S8_M_18->SetBinContent(4,0.0858284347251);
  S8_M_18->SetBinContent(5,0.144211187869);
  S8_M_18->SetBinContent(6,0.204142760673);
  S8_M_18->SetBinContent(7,0.187683341779);
  S8_M_18->SetBinContent(8,0.249376907148);
  S8_M_18->SetBinContent(9,0.289594198077);
  S8_M_18->SetBinContent(10,0.278534384136);
  S8_M_18->SetBinContent(11,0.310977873375);
  S8_M_18->SetBinContent(12,0.374113420494);
  S8_M_18->SetBinContent(13,0.416224027551);
  S8_M_18->SetBinContent(14,0.385504120778);
  S8_M_18->SetBinContent(15,0.362691602372);
  S8_M_18->SetBinContent(16,0.225201521739);
  S8_M_18->SetBinContent(17,0.178216163928);
  S8_M_18->SetBinContent(18,0.115029162365);
  S8_M_18->SetBinContent(19,0.0664230681137);
  S8_M_18->SetBinContent(20,0.0469646440171);
  S8_M_18->SetBinContent(21,0.105312570328); // overflow
  S8_M_18->SetEntries(2542);
  // Style
  S8_M_18->SetLineColor(19);
  S8_M_18->SetLineStyle(1);
  S8_M_18->SetLineWidth(1);
  S8_M_18->SetFillColor(0);
  S8_M_18->SetFillStyle(1001);

  // Creating a new TH1F
  TH1F* S8_M_19 = new TH1F("S8_M_19","S8_M_19",20,750.0,6000.0);
  // Content
  S8_M_19->SetBinContent(0,0.0); // underflow
  S8_M_19->SetBinContent(1,0.0);
  S8_M_19->SetBinContent(2,0.0);
  S8_M_19->SetBinContent(3,0.00852161114693);
  S8_M_19->SetBinContent(4,0.00639111008164);
  S8_M_19->SetBinContent(5,0.019034569823);
  S8_M_19->SetBinContent(6,0.0191432720387);
  S8_M_19->SetBinContent(7,0.0190600944084);
  S8_M_19->SetBinContent(8,0.0212584383073);
  S8_M_19->SetBinContent(9,0.0298214801327);
  S8_M_19->SetBinContent(10,0.025571547565);
  S8_M_19->SetBinContent(11,0.0340316558201);
  S8_M_19->SetBinContent(12,0.0127111655974);
  S8_M_19->SetBinContent(13,0.0191208433672);
  S8_M_19->SetBinContent(14,0.025566346875);
  S8_M_19->SetBinContent(15,0.0127869041252);
  S8_M_19->SetBinContent(16,0.0339612404825);
  S8_M_19->SetBinContent(17,0.0404481824643);
  S8_M_19->SetBinContent(18,0.0276668019841);
  S8_M_19->SetBinContent(19,0.03193409617);
  S8_M_19->SetBinContent(20,0.0212907004033);
  S8_M_19->SetBinContent(21,0.0275491349816); // overflow
  S8_M_19->SetEntries(205);
  // Style
  S8_M_19->SetLineColor(20);
  S8_M_19->SetLineStyle(1);
  S8_M_19->SetLineWidth(1);
  S8_M_19->SetFillColor(0);
  S8_M_19->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_16","mystack");
  stack->Add(S8_M_0);
  stack->Add(S8_M_1);
  stack->Add(S8_M_2);
  stack->Add(S8_M_3);
  stack->Add(S8_M_4);
  stack->Add(S8_M_5);
  stack->Add(S8_M_6);
  stack->Add(S8_M_7);
  stack->Add(S8_M_8);
  stack->Add(S8_M_9);
  stack->Add(S8_M_10);
  stack->Add(S8_M_11);
  stack->Add(S8_M_12);
  stack->Add(S8_M_13);
  stack->Add(S8_M_14);
  stack->Add(S8_M_15);
  stack->Add(S8_M_16);
  stack->Add(S8_M_17);
  stack->Add(S8_M_18);
  stack->Add(S8_M_19);
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
  stack->GetXaxis()->SetTitle("M [ j_{1} , j_{2} ]   ( GeV ) ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(0);

  // Creating a TLegend
  TLegend* legend = new TLegend(.73,.5,.97,.95);
  legend->AddEntry(S8_M_0,"signal_1pt8TeVL");
  legend->AddEntry(S8_M_1,"signal_2TeVL");
  legend->AddEntry(S8_M_2,"signal_2pt2TeVL");
  legend->AddEntry(S8_M_3,"signal_2pt4TeVL");
  legend->AddEntry(S8_M_4,"bg_dip_0_100");
  legend->AddEntry(S8_M_5,"bg_dip_100_200");
  legend->AddEntry(S8_M_6,"bg_dip_200_400");
  legend->AddEntry(S8_M_7,"bg_dip_400_600");
  legend->AddEntry(S8_M_8,"bg_dip_600_800");
  legend->AddEntry(S8_M_9,"bg_dip_800_1200");
  legend->AddEntry(S8_M_10,"bg_dip_1200_1600");
  legend->AddEntry(S8_M_11,"bg_dip_1600_inf");
  legend->AddEntry(S8_M_12,"bg_vbf_0_100");
  legend->AddEntry(S8_M_13,"bg_vbf_100_200");
  legend->AddEntry(S8_M_14,"bg_vbf_200_400");
  legend->AddEntry(S8_M_15,"bg_vbf_400_600");
  legend->AddEntry(S8_M_16,"bg_vbf_600_800");
  legend->AddEntry(S8_M_17,"bg_vbf_800_1200");
  legend->AddEntry(S8_M_18,"bg_vbf_1200_1600");
  legend->AddEntry(S8_M_19,"bg_vbf_1600_inf");
  legend->SetFillColor(0);
  legend->SetTextSize(0.05);
  legend->SetTextFont(22);
  legend->SetY1(TMath::Max(0.15,0.97-0.10*legend->GetListOfPrimitives()->GetSize()));
  legend->Draw();

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_7.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_7.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_7.eps");

}
