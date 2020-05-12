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
  S11_PT_0->SetBinContent(1,3.9429591079);
  S11_PT_0->SetBinContent(2,21.008505637);
  S11_PT_0->SetBinContent(3,38.5109452805);
  S11_PT_0->SetBinContent(4,52.4016698866);
  S11_PT_0->SetBinContent(5,62.7317630806);
  S11_PT_0->SetBinContent(6,70.2628301871);
  S11_PT_0->SetBinContent(7,75.2544267099);
  S11_PT_0->SetBinContent(8,78.2856656301);
  S11_PT_0->SetBinContent(9,80.6983365744);
  S11_PT_0->SetBinContent(10,80.7519825757);
  S11_PT_0->SetBinContent(11,80.9702042753);
  S11_PT_0->SetBinContent(12,80.6252628856);
  S11_PT_0->SetBinContent(13,77.842026791);
  S11_PT_0->SetBinContent(14,76.4049375615);
  S11_PT_0->SetBinContent(15,74.530165718);
  S11_PT_0->SetBinContent(16,71.1247239528);
  S11_PT_0->SetBinContent(17,68.4662088149);
  S11_PT_0->SetBinContent(18,65.3787655148);
  S11_PT_0->SetBinContent(19,63.1495782858);
  S11_PT_0->SetBinContent(20,60.1743438722);
  S11_PT_0->SetBinContent(21,57.6857210632);
  S11_PT_0->SetBinContent(22,54.5605416788);
  S11_PT_0->SetBinContent(23,51.9945279172);
  S11_PT_0->SetBinContent(24,49.9076504978);
  S11_PT_0->SetBinContent(25,46.9455677492);
  S11_PT_0->SetBinContent(26,44.7397257249);
  S11_PT_0->SetBinContent(27,42.610235312);
  S11_PT_0->SetBinContent(28,39.8179689404);
  S11_PT_0->SetBinContent(29,38.5244886972);
  S11_PT_0->SetBinContent(30,36.3504745017);
  S11_PT_0->SetBinContent(31,34.1063687275);
  S11_PT_0->SetBinContent(32,32.1769395237);
  S11_PT_0->SetBinContent(33,30.289647615);
  S11_PT_0->SetBinContent(34,28.7622476209);
  S11_PT_0->SetBinContent(35,27.3358516145);
  S11_PT_0->SetBinContent(36,24.9303601202);
  S11_PT_0->SetBinContent(37,24.0083964245);
  S11_PT_0->SetBinContent(38,22.3503792104);
  S11_PT_0->SetBinContent(39,21.4835325837);
  S11_PT_0->SetBinContent(40,20.4929803566);
  S11_PT_0->SetBinContent(41,18.8507171583);
  S11_PT_0->SetBinContent(42,18.2101910985);
  S11_PT_0->SetBinContent(43,17.1741317121);
  S11_PT_0->SetBinContent(44,16.3387811244);
  S11_PT_0->SetBinContent(45,15.2447105032);
  S11_PT_0->SetBinContent(46,14.371519897);
  S11_PT_0->SetBinContent(47,13.182389521);
  S11_PT_0->SetBinContent(48,12.2113968979);
  S11_PT_0->SetBinContent(49,11.5896069638);
  S11_PT_0->SetBinContent(50,11.1949930546);
  S11_PT_0->SetBinContent(51,10.7675679398);
  S11_PT_0->SetBinContent(52,9.66916406485);
  S11_PT_0->SetBinContent(53,9.30667779436);
  S11_PT_0->SetBinContent(54,8.81012848775);
  S11_PT_0->SetBinContent(55,8.143411027);
  S11_PT_0->SetBinContent(56,7.50044651257);
  S11_PT_0->SetBinContent(57,6.98951831873);
  S11_PT_0->SetBinContent(58,6.56941656267);
  S11_PT_0->SetBinContent(59,6.36030908674);
  S11_PT_0->SetBinContent(60,6.14664050147);
  S11_PT_0->SetBinContent(61,5.53382487986);
  S11_PT_0->SetBinContent(62,5.31982450487);
  S11_PT_0->SetBinContent(63,4.66493954515);
  S11_PT_0->SetBinContent(64,4.58857993886);
  S11_PT_0->SetBinContent(65,4.08941229164);
  S11_PT_0->SetBinContent(66,3.92673938732);
  S11_PT_0->SetBinContent(67,3.85231455484);
  S11_PT_0->SetBinContent(68,3.63646775004);
  S11_PT_0->SetBinContent(69,3.35096029342);
  S11_PT_0->SetBinContent(70,2.92599601903);
  S11_PT_0->SetBinContent(71,2.9537772124);
  S11_PT_0->SetBinContent(72,2.6239610369);
  S11_PT_0->SetBinContent(73,2.38934772557);
  S11_PT_0->SetBinContent(74,2.2709987305);
  S11_PT_0->SetBinContent(75,2.13854347542);
  S11_PT_0->SetBinContent(76,2.08061978517);
  S11_PT_0->SetBinContent(77,1.80429530874);
  S11_PT_0->SetBinContent(78,1.73685285111);
  S11_PT_0->SetBinContent(79,1.62319888052);
  S11_PT_0->SetBinContent(80,1.49313051272);
  S11_PT_0->SetBinContent(81,18.8860667551); // overflow
  S11_PT_0->SetEntries(999999);
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
