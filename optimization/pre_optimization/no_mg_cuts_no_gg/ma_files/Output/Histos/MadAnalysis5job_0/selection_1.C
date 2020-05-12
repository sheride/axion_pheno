void selection_1()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo3","canvas_plotflow_tempo3",0,0,700,500);
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
  TH1F* S2_ETA_0 = new TH1F("S2_ETA_0","S2_ETA_0",160,-8.0,8.0);
  // Content
  S2_ETA_0->SetBinContent(0,0.0); // underflow
  S2_ETA_0->SetBinContent(1,0.0);
  S2_ETA_0->SetBinContent(2,0.0);
  S2_ETA_0->SetBinContent(3,0.0);
  S2_ETA_0->SetBinContent(4,0.0);
  S2_ETA_0->SetBinContent(5,0.0);
  S2_ETA_0->SetBinContent(6,0.0);
  S2_ETA_0->SetBinContent(7,0.0);
  S2_ETA_0->SetBinContent(8,0.0);
  S2_ETA_0->SetBinContent(9,0.0);
  S2_ETA_0->SetBinContent(10,0.0);
  S2_ETA_0->SetBinContent(11,0.0);
  S2_ETA_0->SetBinContent(12,0.0);
  S2_ETA_0->SetBinContent(13,0.0);
  S2_ETA_0->SetBinContent(14,0.0);
  S2_ETA_0->SetBinContent(15,0.0);
  S2_ETA_0->SetBinContent(16,0.0);
  S2_ETA_0->SetBinContent(17,0.0);
  S2_ETA_0->SetBinContent(18,0.0);
  S2_ETA_0->SetBinContent(19,0.0);
  S2_ETA_0->SetBinContent(20,0.0);
  S2_ETA_0->SetBinContent(21,0.0);
  S2_ETA_0->SetBinContent(22,0.0);
  S2_ETA_0->SetBinContent(23,0.0);
  S2_ETA_0->SetBinContent(24,0.0);
  S2_ETA_0->SetBinContent(25,0.0);
  S2_ETA_0->SetBinContent(26,0.0);
  S2_ETA_0->SetBinContent(27,0.0);
  S2_ETA_0->SetBinContent(28,0.0);
  S2_ETA_0->SetBinContent(29,0.0);
  S2_ETA_0->SetBinContent(30,0.0);
  S2_ETA_0->SetBinContent(31,0.534109117962);
  S2_ETA_0->SetBinContent(32,0.617641380894);
  S2_ETA_0->SetBinContent(33,0.822038647805);
  S2_ETA_0->SetBinContent(34,0.975227966832);
  S2_ETA_0->SetBinContent(35,1.33286572034);
  S2_ETA_0->SetBinContent(36,1.57432230158);
  S2_ETA_0->SetBinContent(37,1.8993894961);
  S2_ETA_0->SetBinContent(38,2.21526331675);
  S2_ETA_0->SetBinContent(39,2.80269264399);
  S2_ETA_0->SetBinContent(40,3.38330549105);
  S2_ETA_0->SetBinContent(41,3.82455625632);
  S2_ETA_0->SetBinContent(42,4.40740288776);
  S2_ETA_0->SetBinContent(43,5.3105865114);
  S2_ETA_0->SetBinContent(44,6.09339841845);
  S2_ETA_0->SetBinContent(45,7.07077102615);
  S2_ETA_0->SetBinContent(46,8.44077081345);
  S2_ETA_0->SetBinContent(47,9.28595519306);
  S2_ETA_0->SetBinContent(48,10.4075244188);
  S2_ETA_0->SetBinContent(49,12.3118375946);
  S2_ETA_0->SetBinContent(50,13.7331568591);
  S2_ETA_0->SetBinContent(51,15.0381298559);
  S2_ETA_0->SetBinContent(52,16.5707226029);
  S2_ETA_0->SetBinContent(53,18.4725413595);
  S2_ETA_0->SetBinContent(54,20.8155205386);
  S2_ETA_0->SetBinContent(55,22.4107495909);
  S2_ETA_0->SetBinContent(56,24.5028157816);
  S2_ETA_0->SetBinContent(57,26.1419490104);
  S2_ETA_0->SetBinContent(58,27.8792720132);
  S2_ETA_0->SetBinContent(59,29.7575336987);
  S2_ETA_0->SetBinContent(60,31.8670568264);
  S2_ETA_0->SetBinContent(61,33.9908189304);
  S2_ETA_0->SetBinContent(62,34.8080850027);
  S2_ETA_0->SetBinContent(63,36.2720372494);
  S2_ETA_0->SetBinContent(64,37.5680279386);
  S2_ETA_0->SetBinContent(65,39.3737116191);
  S2_ETA_0->SetBinContent(66,40.3732142023);
  S2_ETA_0->SetBinContent(67,41.1319733523);
  S2_ETA_0->SetBinContent(68,42.3389284663);
  S2_ETA_0->SetBinContent(69,42.4617306426);
  S2_ETA_0->SetBinContent(70,43.2633426354);
  S2_ETA_0->SetBinContent(71,43.1126781164);
  S2_ETA_0->SetBinContent(72,43.9695350987);
  S2_ETA_0->SetBinContent(73,43.6885931406);
  S2_ETA_0->SetBinContent(74,43.5742655936);
  S2_ETA_0->SetBinContent(75,44.8861941825);
  S2_ETA_0->SetBinContent(76,44.0872604923);
  S2_ETA_0->SetBinContent(77,44.0855815563);
  S2_ETA_0->SetBinContent(78,44.1155225817);
  S2_ETA_0->SetBinContent(79,43.4636956653);
  S2_ETA_0->SetBinContent(80,44.2411229847);
  S2_ETA_0->SetBinContent(81,43.6857149646);
  S2_ETA_0->SetBinContent(82,43.8828700211);
  S2_ETA_0->SetBinContent(83,43.738681398);
  S2_ETA_0->SetBinContent(84,44.094016211);
  S2_ETA_0->SetBinContent(85,44.2663469995);
  S2_ETA_0->SetBinContent(86,44.3851916838);
  S2_ETA_0->SetBinContent(87,44.7679491182);
  S2_ETA_0->SetBinContent(88,44.2737822875);
  S2_ETA_0->SetBinContent(89,43.608763731);
  S2_ETA_0->SetBinContent(90,43.4599780213);
  S2_ETA_0->SetBinContent(91,42.8824640104);
  S2_ETA_0->SetBinContent(92,42.6687594418);
  S2_ETA_0->SetBinContent(93,42.1269428084);
  S2_ETA_0->SetBinContent(94,41.2053668405);
  S2_ETA_0->SetBinContent(95,40.0720850375);
  S2_ETA_0->SetBinContent(96,39.2325930504);
  S2_ETA_0->SetBinContent(97,37.9971240067);
  S2_ETA_0->SetBinContent(98,36.8630027356);
  S2_ETA_0->SetBinContent(99,34.9060789009);
  S2_ETA_0->SetBinContent(100,33.7988166084);
  S2_ETA_0->SetBinContent(101,31.5437816962);
  S2_ETA_0->SetBinContent(102,30.0224977825);
  S2_ETA_0->SetBinContent(103,28.0257591796);
  S2_ETA_0->SetBinContent(104,25.7756691337);
  S2_ETA_0->SetBinContent(105,24.1776618421);
  S2_ETA_0->SetBinContent(106,21.925181311);
  S2_ETA_0->SetBinContent(107,20.8850884512);
  S2_ETA_0->SetBinContent(108,18.261167314);
  S2_ETA_0->SetBinContent(109,16.7612738444);
  S2_ETA_0->SetBinContent(110,15.1794802776);
  S2_ETA_0->SetBinContent(111,13.6767925789);
  S2_ETA_0->SetBinContent(112,11.859104506);
  S2_ETA_0->SetBinContent(113,10.7584180462);
  S2_ETA_0->SetBinContent(114,9.18177321651);
  S2_ETA_0->SetBinContent(115,8.07173668218);
  S2_ETA_0->SetBinContent(116,7.06854443721);
  S2_ETA_0->SetBinContent(117,6.26521353371);
  S2_ETA_0->SetBinContent(118,5.23610970973);
  S2_ETA_0->SetBinContent(119,4.30051062881);
  S2_ETA_0->SetBinContent(120,3.83169613155);
  S2_ETA_0->SetBinContent(121,3.18823871111);
  S2_ETA_0->SetBinContent(122,2.75174653017);
  S2_ETA_0->SetBinContent(123,2.34092048378);
  S2_ETA_0->SetBinContent(124,1.83918365047);
  S2_ETA_0->SetBinContent(125,1.61639883634);
  S2_ETA_0->SetBinContent(126,1.22596466696);
  S2_ETA_0->SetBinContent(127,1.05886576288);
  S2_ETA_0->SetBinContent(128,0.880045886762);
  S2_ETA_0->SetBinContent(129,0.692090200295);
  S2_ETA_0->SetBinContent(130,0.487608187089);
  S2_ETA_0->SetBinContent(131,0.0);
  S2_ETA_0->SetBinContent(132,0.0);
  S2_ETA_0->SetBinContent(133,0.0);
  S2_ETA_0->SetBinContent(134,0.0);
  S2_ETA_0->SetBinContent(135,0.0);
  S2_ETA_0->SetBinContent(136,0.0);
  S2_ETA_0->SetBinContent(137,0.0);
  S2_ETA_0->SetBinContent(138,0.0);
  S2_ETA_0->SetBinContent(139,0.0);
  S2_ETA_0->SetBinContent(140,0.0);
  S2_ETA_0->SetBinContent(141,0.0);
  S2_ETA_0->SetBinContent(142,0.0);
  S2_ETA_0->SetBinContent(143,0.0);
  S2_ETA_0->SetBinContent(144,0.0);
  S2_ETA_0->SetBinContent(145,0.0);
  S2_ETA_0->SetBinContent(146,0.0);
  S2_ETA_0->SetBinContent(147,0.0);
  S2_ETA_0->SetBinContent(148,0.0);
  S2_ETA_0->SetBinContent(149,0.0);
  S2_ETA_0->SetBinContent(150,0.0);
  S2_ETA_0->SetBinContent(151,0.0);
  S2_ETA_0->SetBinContent(152,0.0);
  S2_ETA_0->SetBinContent(153,0.0);
  S2_ETA_0->SetBinContent(154,0.0);
  S2_ETA_0->SetBinContent(155,0.0);
  S2_ETA_0->SetBinContent(156,0.0);
  S2_ETA_0->SetBinContent(157,0.0);
  S2_ETA_0->SetBinContent(158,0.0);
  S2_ETA_0->SetBinContent(159,0.0);
  S2_ETA_0->SetBinContent(160,0.0);
  S2_ETA_0->SetBinContent(161,0.0); // overflow
  S2_ETA_0->SetEntries(999999);
  // Style
  S2_ETA_0->SetLineColor(9);
  S2_ETA_0->SetLineStyle(1);
  S2_ETA_0->SetLineWidth(1);
  S2_ETA_0->SetFillColor(9);
  S2_ETA_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_4","mystack");
  stack->Add(S2_ETA_0);
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
  stack->GetXaxis()->SetTitle("#eta [ j_{1} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(0);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_1.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_1.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_1.eps");

}
