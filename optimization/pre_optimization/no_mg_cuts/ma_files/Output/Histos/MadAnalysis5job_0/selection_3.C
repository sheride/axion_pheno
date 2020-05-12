void selection_3()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo7","canvas_plotflow_tempo7",0,0,700,500);
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
  TH1F* S4_PT_0 = new TH1F("S4_PT_0","S4_PT_0",100,0.0,1000.0);
  // Content
  S4_PT_0->SetBinContent(0,0.0); // underflow
  S4_PT_0->SetBinContent(1,0.0);
  S4_PT_0->SetBinContent(2,0.0);
  S4_PT_0->SetBinContent(3,666.532051402);
  S4_PT_0->SetBinContent(4,738.844456979);
  S4_PT_0->SetBinContent(5,716.836455282);
  S4_PT_0->SetBinContent(6,792.292861101);
  S4_PT_0->SetBinContent(7,609.939647038);
  S4_PT_0->SetBinContent(8,779.716860131);
  S4_PT_0->SetBinContent(9,754.564858191);
  S4_PT_0->SetBinContent(10,701.11645407);
  S4_PT_0->SetBinContent(11,672.820051887);
  S4_PT_0->SetBinContent(12,726.268456009);
  S4_PT_0->SetBinContent(13,773.428859646);
  S4_PT_0->SetBinContent(14,638.23604922);
  S4_PT_0->SetBinContent(15,628.804048493);
  S4_PT_0->SetBinContent(16,710.548454797);
  S4_PT_0->SetBinContent(17,616.227647523);
  S4_PT_0->SetBinContent(18,609.939647038);
  S4_PT_0->SetBinContent(19,647.668049948);
  S4_PT_0->SetBinContent(20,635.092048978);
  S4_PT_0->SetBinContent(21,625.66004825);
  S4_PT_0->SetBinContent(22,515.619239764);
  S4_PT_0->SetBinContent(23,644.524049705);
  S4_PT_0->SetBinContent(24,613.083647281);
  S4_PT_0->SetBinContent(25,531.339240976);
  S4_PT_0->SetBinContent(26,509.331239279);
  S4_PT_0->SetBinContent(27,465.314835885);
  S4_PT_0->SetBinContent(28,553.347642674);
  S4_PT_0->SetBinContent(29,597.363646068);
  S4_PT_0->SetBinContent(30,484.178837339);
  S4_PT_0->SetBinContent(31,493.611238067);
  S4_PT_0->SetBinContent(32,443.306834187);
  S4_PT_0->SetBinContent(33,446.45083443);
  S4_PT_0->SetBinContent(34,449.594834672);
  S4_PT_0->SetBinContent(35,493.611238067);
  S4_PT_0->SetBinContent(36,405.578431278);
  S4_PT_0->SetBinContent(37,320.689984731);
  S4_PT_0->SetBinContent(38,374.138348853);
  S4_PT_0->SetBinContent(39,355.274227398);
  S4_PT_0->SetBinContent(40,399.290470793);
  S4_PT_0->SetBinContent(41,370.994308611);
  S4_PT_0->SetBinContent(42,292.393822549);
  S4_PT_0->SetBinContent(43,308.113903761);
  S4_PT_0->SetBinContent(44,298.681863034);
  S4_PT_0->SetBinContent(45,282.961781822);
  S4_PT_0->SetBinContent(46,292.393822549);
  S4_PT_0->SetBinContent(47,333.266065701);
  S4_PT_0->SetBinContent(48,304.969903519);
  S4_PT_0->SetBinContent(49,251.521579397);
  S4_PT_0->SetBinContent(50,257.809619882);
  S4_PT_0->SetBinContent(51,270.385700852);
  S4_PT_0->SetBinContent(52,223.225377215);
  S4_PT_0->SetBinContent(53,160.345012366);
  S4_PT_0->SetBinContent(54,232.657457942);
  S4_PT_0->SetBinContent(55,201.217255518);
  S4_PT_0->SetBinContent(56,198.073255275);
  S4_PT_0->SetBinContent(57,179.20913382);
  S4_PT_0->SetBinContent(58,185.497174305);
  S4_PT_0->SetBinContent(59,198.073255275);
  S4_PT_0->SetBinContent(60,179.20913382);
  S4_PT_0->SetBinContent(61,185.497174305);
  S4_PT_0->SetBinContent(62,172.921093336);
  S4_PT_0->SetBinContent(63,182.353134063);
  S4_PT_0->SetBinContent(64,141.480890911);
  S4_PT_0->SetBinContent(65,116.328728971);
  S4_PT_0->SetBinContent(66,116.328728971);
  S4_PT_0->SetBinContent(67,182.353134063);
  S4_PT_0->SetBinContent(68,116.328728971);
  S4_PT_0->SetBinContent(69,138.336850668);
  S4_PT_0->SetBinContent(70,94.3206072739);
  S4_PT_0->SetBinContent(71,116.328728971);
  S4_PT_0->SetBinContent(72,110.040688486);
  S4_PT_0->SetBinContent(73,110.040688486);
  S4_PT_0->SetBinContent(74,78.6004860616);
  S4_PT_0->SetBinContent(75,94.3206072739);
  S4_PT_0->SetBinContent(76,100.608607759);
  S4_PT_0->SetBinContent(77,100.608607759);
  S4_PT_0->SetBinContent(78,100.608607759);
  S4_PT_0->SetBinContent(79,110.040688486);
  S4_PT_0->SetBinContent(80,81.7445263041);
  S4_PT_0->SetBinContent(81,81.7445263041);
  S4_PT_0->SetBinContent(82,94.3206072739);
  S4_PT_0->SetBinContent(83,72.3124455767);
  S4_PT_0->SetBinContent(84,69.1684453342);
  S4_PT_0->SetBinContent(85,75.4564858191);
  S4_PT_0->SetBinContent(86,69.1684453342);
  S4_PT_0->SetBinContent(87,40.872243152);
  S4_PT_0->SetBinContent(88,56.5923643644);
  S4_PT_0->SetBinContent(89,56.5923643644);
  S4_PT_0->SetBinContent(90,47.160283637);
  S4_PT_0->SetBinContent(91,50.3043238794);
  S4_PT_0->SetBinContent(92,15.7200972123);
  S4_PT_0->SetBinContent(93,56.5923643644);
  S4_PT_0->SetBinContent(94,31.4401944246);
  S4_PT_0->SetBinContent(95,53.4483241219);
  S4_PT_0->SetBinContent(96,50.3043238794);
  S4_PT_0->SetBinContent(97,28.2961781822);
  S4_PT_0->SetBinContent(98,22.0081376972);
  S4_PT_0->SetBinContent(99,40.872243152);
  S4_PT_0->SetBinContent(100,25.1521579397);
  S4_PT_0->SetBinContent(101,789.148860859); // overflow
  S4_PT_0->SetEntries(9999);
  // Style
  S4_PT_0->SetLineColor(9);
  S4_PT_0->SetLineStyle(1);
  S4_PT_0->SetLineWidth(1);
  S4_PT_0->SetFillColor(9);
  S4_PT_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_8","mystack");
  stack->Add(S4_PT_0);
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
  stack->GetXaxis()->SetTitle("p_{T} [ j_{2} ]   ( GeV ) ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(0);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_3.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_3.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_3.eps");

}
