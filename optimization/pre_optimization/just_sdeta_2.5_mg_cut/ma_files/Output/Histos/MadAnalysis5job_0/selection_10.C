void selection_10()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo21","canvas_plotflow_tempo21",0,0,700,500);
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
  TH1F* S11_PT_0 = new TH1F("S11_PT_0","S11_PT_0",80,0.0,2000.0);
  // Content
  S11_PT_0->SetBinContent(0,0.0); // underflow
  S11_PT_0->SetBinContent(1,1.48657968142);
  S11_PT_0->SetBinContent(2,15.9807288752);
  S11_PT_0->SetBinContent(3,33.8196818522);
  S11_PT_0->SetBinContent(4,46.0839625239);
  S11_PT_0->SetBinContent(5,56.8616831142);
  S11_PT_0->SetBinContent(6,74.7006040912);
  S11_PT_0->SetBinContent(7,82.5051645186);
  S11_PT_0->SetBinContent(8,103.688925679);
  S11_PT_0->SetBinContent(9,115.95320635);
  S11_PT_0->SetBinContent(10,113.723326228);
  S11_PT_0->SetBinContent(11,128.589127042);
  S11_PT_0->SetBinContent(12,122.271166696);
  S11_PT_0->SetBinContent(13,118.554726493);
  S11_PT_0->SetBinContent(14,124.872686839);
  S11_PT_0->SetBinContent(15,122.271166696);
  S11_PT_0->SetBinContent(16,119.298006534);
  S11_PT_0->SetBinContent(17,119.669646554);
  S11_PT_0->SetBinContent(18,117.439766432);
  S11_PT_0->SetBinContent(19,121.156246635);
  S11_PT_0->SetBinContent(20,115.20992631);
  S11_PT_0->SetBinContent(21,110.006886025);
  S11_PT_0->SetBinContent(22,104.80384574);
  S11_PT_0->SetBinContent(23,101.087405536);
  S11_PT_0->SetBinContent(24,89.194764885);
  S11_PT_0->SetBinContent(25,106.290445821);
  S11_PT_0->SetBinContent(26,87.7082048036);
  S11_PT_0->SetBinContent(27,69.8692438266);
  S11_PT_0->SetBinContent(28,86.9648847628);
  S11_PT_0->SetBinContent(29,78.4170842947);
  S11_PT_0->SetBinContent(30,73.5856840301);
  S11_PT_0->SetBinContent(31,60.9497633381);
  S11_PT_0->SetBinContent(32,59.0915232363);
  S11_PT_0->SetBinContent(33,61.6930433788);
  S11_PT_0->SetBinContent(34,64.2945635212);
  S11_PT_0->SetBinContent(35,48.6854826664);
  S11_PT_0->SetBinContent(36,43.8540824018);
  S11_PT_0->SetBinContent(37,44.9690424628);
  S11_PT_0->SetBinContent(38,45.3406824832);
  S11_PT_0->SetBinContent(39,41.2525622593);
  S11_PT_0->SetBinContent(40,36.0495539743);
  S11_PT_0->SetBinContent(41,36.0495539743);
  S11_PT_0->SetBinContent(42,28.2450095469);
  S11_PT_0->SetBinContent(43,27.1300774858);
  S11_PT_0->SetBinContent(44,19.3255330584);
  S11_PT_0->SetBinContent(45,28.6166535673);
  S11_PT_0->SetBinContent(46,22.2986932212);
  S11_PT_0->SetBinContent(47,21.5554011805);
  S11_PT_0->SetBinContent(48,23.7852733027);
  S11_PT_0->SetBinContent(49,18.9538890381);
  S11_PT_0->SetBinContent(50,16.7240209159);
  S11_PT_0->SetBinContent(51,14.1225047735);
  S11_PT_0->SetBinContent(52,11.8926366513);
  S11_PT_0->SetBinContent(53,13.3792167327);
  S11_PT_0->SetBinContent(54,14.1225047735);
  S11_PT_0->SetBinContent(55,11.1493446106);
  S11_PT_0->SetBinContent(56,9.66276852921);
  S11_PT_0->SetBinContent(57,11.520992631);
  S11_PT_0->SetBinContent(58,10.0344125496);
  S11_PT_0->SetBinContent(59,9.29112050885);
  S11_PT_0->SetBinContent(60,10.4060565699);
  S11_PT_0->SetBinContent(61,6.31796434602);
  S11_PT_0->SetBinContent(62,6.68960836637);
  S11_PT_0->SetBinContent(63,5.57467230531);
  S11_PT_0->SetBinContent(64,4.8313842646);
  S11_PT_0->SetBinContent(65,4.8313842646);
  S11_PT_0->SetBinContent(66,2.60151414248);
  S11_PT_0->SetBinContent(67,4.08809222389);
  S11_PT_0->SetBinContent(68,2.60151414248);
  S11_PT_0->SetBinContent(69,5.94631632566);
  S11_PT_0->SetBinContent(70,2.97315896283);
  S11_PT_0->SetBinContent(71,3.71644860354);
  S11_PT_0->SetBinContent(72,3.71644860354);
  S11_PT_0->SetBinContent(73,2.97315896283);
  S11_PT_0->SetBinContent(74,2.60151414248);
  S11_PT_0->SetBinContent(75,1.85822450177);
  S11_PT_0->SetBinContent(76,3.71644860354);
  S11_PT_0->SetBinContent(77,0.743289640708);
  S11_PT_0->SetBinContent(78,2.60151414248);
  S11_PT_0->SetBinContent(79,1.48657968142);
  S11_PT_0->SetBinContent(80,1.48657968142);
  S11_PT_0->SetBinContent(81,18.2105969973); // overflow
  S11_PT_0->SetEntries(9999);
  // Style
  S11_PT_0->SetLineColor(9);
  S11_PT_0->SetLineStyle(1);
  S11_PT_0->SetLineWidth(1);
  S11_PT_0->SetFillColor(9);
  S11_PT_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_22","mystack");
  stack->Add(S11_PT_0);
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
  stack->GetXaxis()->SetTitle("p_{T} [ a_{1} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(0);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_10.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_10.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_10.eps");

}
