void selection_0()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo1","canvas_plotflow_tempo1",0,0,700,500);
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
  TH1F* S1_ETA_0 = new TH1F("S1_ETA_0","S1_ETA_0",100,-8.0,8.0);
  // Content
  S1_ETA_0->SetBinContent(0,0.0163763339764); // underflow
  S1_ETA_0->SetBinContent(1,0.0040940844941);
  S1_ETA_0->SetBinContent(2,0.00818816898821);
  S1_ETA_0->SetBinContent(3,0.00818816898821);
  S1_ETA_0->SetBinContent(4,0.0122822534823);
  S1_ETA_0->SetBinContent(5,0.0368467564469);
  S1_ETA_0->SetBinContent(6,0.0163763339764);
  S1_ETA_0->SetBinContent(7,0.0040940844941);
  S1_ETA_0->SetBinContent(8,0.0204704184705);
  S1_ETA_0->SetBinContent(9,0.0491289979293);
  S1_ETA_0->SetBinContent(10,0.0614112674116);
  S1_ETA_0->SetBinContent(11,0.077787613388);
  S1_ETA_0->SetBinContent(12,0.110540265341);
  S1_ETA_0->SetBinContent(13,0.188327878729);
  S1_ETA_0->SetBinContent(14,0.176045609246);
  S1_ETA_0->SetBinContent(15,0.253833222634);
  S1_ETA_0->SetBinContent(16,0.40940844941);
  S1_ETA_0->SetBinContent(17,0.470819596822);
  S1_ETA_0->SetBinContent(18,0.765593744398);
  S1_ETA_0->SetBinContent(19,1.09721466042);
  S1_ETA_0->SetBinContent(20,1.40427079748);
  S1_ETA_0->SetBinContent(21,1.76864408545);
  S1_ETA_0->SetBinContent(22,2.54652021933);
  S1_ETA_0->SetBinContent(23,3.27117319879);
  S1_ETA_0->SetBinContent(24,4.515776133);
  S1_ETA_0->SetBinContent(25,5.96507889191);
  S1_ETA_0->SetBinContent(26,7.41848164732);
  S1_ETA_0->SetBinContent(27,9.63337975063);
  S1_ETA_0->SetBinContent(28,12.3518494227);
  S1_ETA_0->SetBinContent(29,15.246366944);
  S1_ETA_0->SetBinContent(30,19.0538676836);
  S1_ETA_0->SetBinContent(31,23.5246078551);
  S1_ETA_0->SetBinContent(32,28.1836758654);
  S1_ETA_0->SetBinContent(33,34.8365621683);
  S1_ETA_0->SetBinContent(34,41.2642846641);
  S1_ETA_0->SetBinContent(35,48.3388386059);
  S1_ETA_0->SetBinContent(36,56.2322318465);
  S1_ETA_0->SetBinContent(37,66.2177032957);
  S1_ETA_0->SetBinContent(38,76.8213742154);
  S1_ETA_0->SetBinContent(39,86.0453663166);
  S1_ETA_0->SetBinContent(40,97.2385967315);
  S1_ETA_0->SetBinContent(41,108.153427385);
  S1_ETA_0->SetBinContent(42,118.888098192);
  S1_ETA_0->SetBinContent(43,128.803969701);
  S1_ETA_0->SetBinContent(44,136.480403127);
  S1_ETA_0->SetBinContent(45,142.744317763);
  S1_ETA_0->SetBinContent(46,147.059514068);
  S1_ETA_0->SetBinContent(47,152.803509149);
  S1_ETA_0->SetBinContent(48,154.756387477);
  S1_ETA_0->SetBinContent(49,155.345906972);
  S1_ETA_0->SetBinContent(50,156.754305766);
  S1_ETA_0->SetBinContent(51,156.705145808);
  S1_ETA_0->SetBinContent(52,155.763506615);
  S1_ETA_0->SetBinContent(53,155.583386769);
  S1_ETA_0->SetBinContent(54,152.365429525);
  S1_ETA_0->SetBinContent(55,149.298952151);
  S1_ETA_0->SetBinContent(56,141.376918934);
  S1_ETA_0->SetBinContent(57,134.404684905);
  S1_ETA_0->SetBinContent(58,127.95241043);
  S1_ETA_0->SetBinContent(59,118.228938757);
  S1_ETA_0->SetBinContent(60,107.915947588);
  S1_ETA_0->SetBinContent(61,96.9724769594);
  S1_ETA_0->SetBinContent(62,85.9143664288);
  S1_ETA_0->SetBinContent(63,76.3505746186);
  S1_ETA_0->SetBinContent(64,66.0867034078);
  S1_ETA_0->SetBinContent(65,56.9691912155);
  S1_ETA_0->SetBinContent(66,48.5107984586);
  S1_ETA_0->SetBinContent(67,41.2315246921);
  S1_ETA_0->SetBinContent(68,34.8611261473);
  S1_ETA_0->SetBinContent(69,28.7036234202);
  S1_ETA_0->SetBinContent(70,23.1725161566);
  S1_ETA_0->SetBinContent(71,18.9637957607);
  S1_ETA_0->SetBinContent(72,15.7049065514);
  S1_ETA_0->SetBinContent(73,12.6630011563);
  S1_ETA_0->SetBinContent(74,9.61290776816);
  S1_ETA_0->SetBinContent(75,7.87701725466);
  S1_ETA_0->SetBinContent(76,5.94051491295);
  S1_ETA_0->SetBinContent(77,4.46255217857);
  S1_ETA_0->SetBinContent(78,3.36124312166);
  S1_ETA_0->SetBinContent(79,2.55061421583);
  S1_ETA_0->SetBinContent(80,1.96516031717);
  S1_ETA_0->SetBinContent(81,1.41245879047);
  S1_ETA_0->SetBinContent(82,0.859757663762);
  S1_ETA_0->SetBinContent(83,0.765593744398);
  S1_ETA_0->SetBinContent(84,0.577265905669);
  S1_ETA_0->SetBinContent(85,0.421690838893);
  S1_ETA_0->SetBinContent(86,0.290679951081);
  S1_ETA_0->SetBinContent(87,0.266115452117);
  S1_ETA_0->SetBinContent(88,0.114634341835);
  S1_ETA_0->SetBinContent(89,0.102352112353);
  S1_ETA_0->SetBinContent(90,0.0982579958585);
  S1_ETA_0->SetBinContent(91,0.106446188847);
  S1_ETA_0->SetBinContent(92,0.0245645029646);
  S1_ETA_0->SetBinContent(93,0.0122822534823);
  S1_ETA_0->SetBinContent(94,0.0327526719528);
  S1_ETA_0->SetBinContent(95,0.0204704184705);
  S1_ETA_0->SetBinContent(96,0.00818816898821);
  S1_ETA_0->SetBinContent(97,0.00818816898821);
  S1_ETA_0->SetBinContent(98,0.0122822534823);
  S1_ETA_0->SetBinContent(99,0.0);
  S1_ETA_0->SetBinContent(100,0.0040940844941);
  S1_ETA_0->SetBinContent(101,0.0163763339764); // overflow
  S1_ETA_0->SetEntries(999999);
  // Style
  S1_ETA_0->SetLineColor(9);
  S1_ETA_0->SetLineStyle(1);
  S1_ETA_0->SetLineWidth(1);
  S1_ETA_0->SetFillColor(9);
  S1_ETA_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_2","mystack");
  stack->Add(S1_ETA_0);
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
  stack->GetXaxis()->SetTitle("#eta [ a_{1} a_{2} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(0);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_0.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_0.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_0.eps");

}
