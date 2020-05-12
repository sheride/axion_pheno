void selection_5()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo11","canvas_plotflow_tempo11",0,0,700,500);
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
  TH1F* S6_PHI_0 = new TH1F("S6_PHI_0","S6_PHI_0",64,-3.2,3.2);
  // Content
  S6_PHI_0->SetBinContent(0,0.0); // underflow
  S6_PHI_0->SetBinContent(1,15.3910857629);
  S6_PHI_0->SetBinContent(2,36.9518534351);
  S6_PHI_0->SetBinContent(3,37.3577721805);
  S6_PHI_0->SetBinContent(4,37.1142345247);
  S6_PHI_0->SetBinContent(5,37.300492482);
  S6_PHI_0->SetBinContent(6,37.2157901629);
  S6_PHI_0->SetBinContent(7,36.7033109511);
  S6_PHI_0->SetBinContent(8,37.3788588167);
  S6_PHI_0->SetBinContent(9,37.0395218745);
  S6_PHI_0->SetBinContent(10,37.0523417498);
  S6_PHI_0->SetBinContent(11,37.0468932028);
  S6_PHI_0->SetBinContent(12,36.9444661169);
  S6_PHI_0->SetBinContent(13,36.8012888568);
  S6_PHI_0->SetBinContent(14,36.7400676562);
  S6_PHI_0->SetBinContent(15,37.0068665701);
  S6_PHI_0->SetBinContent(16,36.5754639753);
  S6_PHI_0->SetBinContent(17,37.2020948424);
  S6_PHI_0->SetBinContent(18,36.5804688034);
  S6_PHI_0->SetBinContent(19,37.0703263519);
  S6_PHI_0->SetBinContent(20,36.9986557737);
  S6_PHI_0->SetBinContent(21,36.8273643312);
  S6_PHI_0->SetBinContent(22,37.2402666507);
  S6_PHI_0->SetBinContent(23,37.0405532208);
  S6_PHI_0->SetBinContent(24,36.8457686673);
  S6_PHI_0->SetBinContent(25,36.8382734175);
  S6_PHI_0->SetBinContent(26,36.70583735);
  S6_PHI_0->SetBinContent(27,37.212004562);
  S6_PHI_0->SetBinContent(28,37.1171206955);
  S6_PHI_0->SetBinContent(29,37.1538094437);
  S6_PHI_0->SetBinContent(30,36.8892611036);
  S6_PHI_0->SetBinContent(31,36.9903330483);
  S6_PHI_0->SetBinContent(32,37.0237838486);
  S6_PHI_0->SetBinContent(33,36.4770023762);
  S6_PHI_0->SetBinContent(34,36.7267840748);
  S6_PHI_0->SetBinContent(35,36.8895249364);
  S6_PHI_0->SetBinContent(36,36.8684143154);
  S6_PHI_0->SetBinContent(37,37.2094861581);
  S6_PHI_0->SetBinContent(38,36.4531894678);
  S6_PHI_0->SetBinContent(39,36.67983383);
  S6_PHI_0->SetBinContent(40,36.9980481588);
  S6_PHI_0->SetBinContent(41,36.7996938676);
  S6_PHI_0->SetBinContent(42,36.8982713932);
  S6_PHI_0->SetBinContent(43,36.9846806306);
  S6_PHI_0->SetBinContent(44,36.7642843087);
  S6_PHI_0->SetBinContent(45,37.2603059506);
  S6_PHI_0->SetBinContent(46,37.2567002358);
  S6_PHI_0->SetBinContent(47,36.7192528478);
  S6_PHI_0->SetBinContent(48,37.060568536);
  S6_PHI_0->SetBinContent(49,36.9286561366);
  S6_PHI_0->SetBinContent(50,37.3161385662);
  S6_PHI_0->SetBinContent(51,36.7192488503);
  S6_PHI_0->SetBinContent(52,36.7635567698);
  S6_PHI_0->SetBinContent(53,37.0675081379);
  S6_PHI_0->SetBinContent(54,36.6637680118);
  S6_PHI_0->SetBinContent(55,36.7962520489);
  S6_PHI_0->SetBinContent(56,37.0986164228);
  S6_PHI_0->SetBinContent(57,36.9796318303);
  S6_PHI_0->SetBinContent(58,36.9368869203);
  S6_PHI_0->SetBinContent(59,36.8219717488);
  S6_PHI_0->SetBinContent(60,36.8703650791);
  S6_PHI_0->SetBinContent(61,37.0931199062);
  S6_PHI_0->SetBinContent(62,37.4858110348);
  S6_PHI_0->SetBinContent(63,36.8196452232);
  S6_PHI_0->SetBinContent(64,15.3470296838);
  S6_PHI_0->SetBinContent(65,0.0); // overflow
  S6_PHI_0->SetEntries(999999);
  // Style
  S6_PHI_0->SetLineColor(9);
  S6_PHI_0->SetLineStyle(1);
  S6_PHI_0->SetLineWidth(1);
  S6_PHI_0->SetFillColor(9);
  S6_PHI_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_12","mystack");
  stack->Add(S6_PHI_0);
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
  stack->GetXaxis()->SetTitle("#phi [ j_{2} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(0);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_5.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_5.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_5.eps");

}
