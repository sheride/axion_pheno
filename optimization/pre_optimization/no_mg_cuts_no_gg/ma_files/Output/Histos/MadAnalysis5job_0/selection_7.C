void selection_7()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo15","canvas_plotflow_tempo15",0,0,700,500);
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
  canvas->SetRightMargin(0.05);
  canvas->SetBottomMargin(0.15);
  canvas->SetTopMargin(0.05);

  // Creating a new TH1F
  TH1F* S8_M_0 = new TH1F("S8_M_0","S8_M_0",160,0.0,3000.0);
  // Content
  S8_M_0->SetBinContent(0,0.0); // underflow
  S8_M_0->SetBinContent(1,0.125410279272);
  S8_M_0->SetBinContent(2,2.26858105124);
  S8_M_0->SetBinContent(3,5.56630426752);
  S8_M_0->SetBinContent(4,13.5887279309);
  S8_M_0->SetBinContent(5,200.664545702);
  S8_M_0->SetBinContent(6,26.2494559963);
  S8_M_0->SetBinContent(7,19.8280976327);
  S8_M_0->SetBinContent(8,21.6626509558);
  S8_M_0->SetBinContent(9,23.1095579558);
  S8_M_0->SetBinContent(10,24.8775894382);
  S8_M_0->SetBinContent(11,25.8634326446);
  S8_M_0->SetBinContent(12,26.8575905815);
  S8_M_0->SetBinContent(13,27.1735823167);
  S8_M_0->SetBinContent(14,28.3233056616);
  S8_M_0->SetBinContent(15,28.9424452722);
  S8_M_0->SetBinContent(16,28.866409461);
  S8_M_0->SetBinContent(17,29.1268364114);
  S8_M_0->SetBinContent(18,29.412199558);
  S8_M_0->SetBinContent(19,29.3140657519);
  S8_M_0->SetBinContent(20,29.4817754632);
  S8_M_0->SetBinContent(21,29.3650174604);
  S8_M_0->SetBinContent(22,29.240088636);
  S8_M_0->SetBinContent(23,28.6760780865);
  S8_M_0->SetBinContent(24,29.1072688127);
  S8_M_0->SetBinContent(25,28.5116263104);
  S8_M_0->SetBinContent(26,28.64997463);
  S8_M_0->SetBinContent(27,28.1164487604);
  S8_M_0->SetBinContent(28,28.3507522669);
  S8_M_0->SetBinContent(29,27.4126268186);
  S8_M_0->SetBinContent(30,27.1063928991);
  S8_M_0->SetBinContent(31,26.6719762175);
  S8_M_0->SetBinContent(32,27.1296341696);
  S8_M_0->SetBinContent(33,26.1303394882);
  S8_M_0->SetBinContent(34,26.1023772098);
  S8_M_0->SetBinContent(35,24.9972136245);
  S8_M_0->SetBinContent(36,25.1093825357);
  S8_M_0->SetBinContent(37,24.9481767024);
  S8_M_0->SetBinContent(38,24.4587388913);
  S8_M_0->SetBinContent(39,23.5740355858);
  S8_M_0->SetBinContent(40,23.8018352143);
  S8_M_0->SetBinContent(41,23.2487537383);
  S8_M_0->SetBinContent(42,22.6822567646);
  S8_M_0->SetBinContent(43,22.9006263695);
  S8_M_0->SetBinContent(44,22.047710918);
  S8_M_0->SetBinContent(45,21.5811825876);
  S8_M_0->SetBinContent(46,21.6629067936);
  S8_M_0->SetBinContent(47,20.6273470958);
  S8_M_0->SetBinContent(48,20.2048588544);
  S8_M_0->SetBinContent(49,20.5000357814);
  S8_M_0->SetBinContent(50,19.7057351818);
  S8_M_0->SetBinContent(51,19.672612174);
  S8_M_0->SetBinContent(52,19.0718089425);
  S8_M_0->SetBinContent(53,18.8301660874);
  S8_M_0->SetBinContent(54,18.5326026729);
  S8_M_0->SetBinContent(55,18.2222393705);
  S8_M_0->SetBinContent(56,17.9221855343);
  S8_M_0->SetBinContent(57,17.3579551242);
  S8_M_0->SetBinContent(58,17.2902780156);
  S8_M_0->SetBinContent(59,16.6545689062);
  S8_M_0->SetBinContent(60,16.6976815829);
  S8_M_0->SetBinContent(61,16.1127642834);
  S8_M_0->SetBinContent(62,15.9647660795);
  S8_M_0->SetBinContent(63,15.76966173);
  S8_M_0->SetBinContent(64,15.6134327425);
  S8_M_0->SetBinContent(65,15.2961578205);
  S8_M_0->SetBinContent(66,14.789622845);
  S8_M_0->SetBinContent(67,14.7155497899);
  S8_M_0->SetBinContent(68,14.1345500076);
  S8_M_0->SetBinContent(69,14.0836902408);
  S8_M_0->SetBinContent(70,13.8129218445);
  S8_M_0->SetBinContent(71,13.6162544855);
  S8_M_0->SetBinContent(72,13.0593434366);
  S8_M_0->SetBinContent(73,13.0665068967);
  S8_M_0->SetBinContent(74,12.4529197671);
  S8_M_0->SetBinContent(75,12.3492894445);
  S8_M_0->SetBinContent(76,12.2631720227);
  S8_M_0->SetBinContent(77,11.7781274273);
  S8_M_0->SetBinContent(78,11.687181066);
  S8_M_0->SetBinContent(79,11.629233791);
  S8_M_0->SetBinContent(80,11.2874464041);
  S8_M_0->SetBinContent(81,11.0204356264);
  S8_M_0->SetBinContent(82,10.7515220546);
  S8_M_0->SetBinContent(83,10.5238463476);
  S8_M_0->SetBinContent(84,10.2565997193);
  S8_M_0->SetBinContent(85,10.0687907462);
  S8_M_0->SetBinContent(86,9.59487909515);
  S8_M_0->SetBinContent(87,9.66291197824);
  S8_M_0->SetBinContent(88,9.45819771911);
  S8_M_0->SetBinContent(89,9.15363873813);
  S8_M_0->SetBinContent(90,9.29311834075);
  S8_M_0->SetBinContent(91,8.83831457975);
  S8_M_0->SetBinContent(92,8.45960659187);
  S8_M_0->SetBinContent(93,8.44334090051);
  S8_M_0->SetBinContent(94,8.52181516621);
  S8_M_0->SetBinContent(95,8.19948744645);
  S8_M_0->SetBinContent(96,7.77912585719);
  S8_M_0->SetBinContent(97,8.09678053856);
  S8_M_0->SetBinContent(98,7.57974421843);
  S8_M_0->SetBinContent(99,7.67703855661);
  S8_M_0->SetBinContent(100,7.4910444333);
  S8_M_0->SetBinContent(101,7.07073880857);
  S8_M_0->SetBinContent(102,6.791939502);
  S8_M_0->SetBinContent(103,6.65742875029);
  S8_M_0->SetBinContent(104,6.80144547744);
  S8_M_0->SetBinContent(105,6.45073574522);
  S8_M_0->SetBinContent(106,6.38800350276);
  S8_M_0->SetBinContent(107,6.36247568142);
  S8_M_0->SetBinContent(108,6.26969448296);
  S8_M_0->SetBinContent(109,5.91214908295);
  S8_M_0->SetBinContent(110,5.67978834521);
  S8_M_0->SetBinContent(111,5.55235710675);
  S8_M_0->SetBinContent(112,5.81000581785);
  S8_M_0->SetBinContent(113,5.58233810582);
  S8_M_0->SetBinContent(114,5.4711165942);
  S8_M_0->SetBinContent(115,5.40378726521);
  S8_M_0->SetBinContent(116,5.10413317568);
  S8_M_0->SetBinContent(117,5.14791742673);
  S8_M_0->SetBinContent(118,5.27579238397);
  S8_M_0->SetBinContent(119,4.86472490442);
  S8_M_0->SetBinContent(120,4.80660174089);
  S8_M_0->SetBinContent(121,4.61165329252);
  S8_M_0->SetBinContent(122,4.53979883141);
  S8_M_0->SetBinContent(123,4.4001273504);
  S8_M_0->SetBinContent(124,4.29117639977);
  S8_M_0->SetBinContent(125,4.28648737151);
  S8_M_0->SetBinContent(126,4.20059380791);
  S8_M_0->SetBinContent(127,3.96141139351);
  S8_M_0->SetBinContent(128,3.70827502264);
  S8_M_0->SetBinContent(129,3.85713148253);
  S8_M_0->SetBinContent(130,3.9314695696);
  S8_M_0->SetBinContent(131,3.90100008012);
  S8_M_0->SetBinContent(132,3.73379444931);
  S8_M_0->SetBinContent(133,3.37606876356);
  S8_M_0->SetBinContent(134,3.43910601272);
  S8_M_0->SetBinContent(135,3.34374964631);
  S8_M_0->SetBinContent(136,3.29507169672);
  S8_M_0->SetBinContent(137,3.43460646438);
  S8_M_0->SetBinContent(138,3.10243178528);
  S8_M_0->SetBinContent(139,2.98395407239);
  S8_M_0->SetBinContent(140,3.00049958641);
  S8_M_0->SetBinContent(141,3.00726609803);
  S8_M_0->SetBinContent(142,2.82151781891);
  S8_M_0->SetBinContent(143,2.82602656142);
  S8_M_0->SetBinContent(144,2.83968790333);
  S8_M_0->SetBinContent(145,2.59617263494);
  S8_M_0->SetBinContent(146,2.53120261071);
  S8_M_0->SetBinContent(147,2.63793376817);
  S8_M_0->SetBinContent(148,2.6311496677);
  S8_M_0->SetBinContent(149,2.53804467445);
  S8_M_0->SetBinContent(150,2.42638663948);
  S8_M_0->SetBinContent(151,2.30128792275);
  S8_M_0->SetBinContent(152,2.25463389047);
  S8_M_0->SetBinContent(153,2.40560341117);
  S8_M_0->SetBinContent(154,2.26170620828);
  S8_M_0->SetBinContent(155,2.21058660613);
  S8_M_0->SetBinContent(156,1.94606305207);
  S8_M_0->SetBinContent(157,1.92503637805);
  S8_M_0->SetBinContent(158,1.93888120368);
  S8_M_0->SetBinContent(159,1.93190282634);
  S8_M_0->SetBinContent(160,1.91799284201);
  S8_M_0->SetBinContent(161,72.8309222627); // overflow
  S8_M_0->SetEntries(999999);
  // Style
  S8_M_0->SetLineColor(9);
  S8_M_0->SetLineStyle(1);
  S8_M_0->SetLineWidth(1);
  S8_M_0->SetFillColor(9);
  S8_M_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_16","mystack");
  stack->Add(S8_M_0);
  stack->Draw("");

  // Y axis
  stack->GetYaxis()->SetLabelSize(0.04);
  stack->GetYaxis()->SetLabelOffset(0.005);
  stack->GetYaxis()->SetTitleSize(0.06);
  stack->GetYaxis()->SetTitleFont(22);
  stack->GetYaxis()->SetTitleOffset(1);
  stack->GetYaxis()->SetTitle("Events  ( L_{int} = 40.0 fb^{-1} )");

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

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_7.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_7.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_7.eps");

}
