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
  S11_PT_0->SetBinContent(1,9.43206096502);
  S11_PT_0->SetBinContent(2,47.1602848251);
  S11_PT_0->SetBinContent(3,144.624894797);
  S11_PT_0->SetBinContent(4,210.649301552);
  S11_PT_0->SetBinContent(5,308.113911524);
  S11_PT_0->SetBinContent(6,389.858439887);
  S11_PT_0->SetBinContent(7,471.602848251);
  S11_PT_0->SetBinContent(8,518.763253076);
  S11_PT_0->SetBinContent(9,707.404472376);
  S11_PT_0->SetBinContent(10,660.244067551);
  S11_PT_0->SetBinContent(11,867.749288782);
  S11_PT_0->SetBinContent(12,836.309285565);
  S11_PT_0->SetBinContent(13,858.317287816);
  S11_PT_0->SetBinContent(14,880.325690068);
  S11_PT_0->SetBinContent(15,899.189691998);
  S11_PT_0->SetBinContent(16,789.14888074);
  S11_PT_0->SetBinContent(17,908.621692963);
  S11_PT_0->SetBinContent(18,852.029287173);
  S11_PT_0->SetBinContent(19,870.893289103);
  S11_PT_0->SetBinContent(20,848.885286851);
  S11_PT_0->SetBinContent(21,852.029287173);
  S11_PT_0->SetBinContent(22,861.461288138);
  S11_PT_0->SetBinContent(23,804.868882348);
  S11_PT_0->SetBinContent(24,767.140878488);
  S11_PT_0->SetBinContent(25,741.988475915);
  S11_PT_0->SetBinContent(26,770.28487881);
  S11_PT_0->SetBinContent(27,792.292881061);
  S11_PT_0->SetBinContent(28,754.564877201);
  S11_PT_0->SetBinContent(29,707.404472376);
  S11_PT_0->SetBinContent(30,691.684470768);
  S11_PT_0->SetBinContent(31,644.524065943);
  S11_PT_0->SetBinContent(32,669.676068516);
  S11_PT_0->SetBinContent(33,591.075660474);
  S11_PT_0->SetBinContent(34,616.227663048);
  S11_PT_0->SetBinContent(35,556.491656936);
  S11_PT_0->SetBinContent(36,471.602848251);
  S11_PT_0->SetBinContent(37,468.458847929);
  S11_PT_0->SetBinContent(38,459.026846964);
  S11_PT_0->SetBinContent(39,503.043251468);
  S11_PT_0->SetBinContent(40,396.146480531);
  S11_PT_0->SetBinContent(41,440.162845034);
  S11_PT_0->SetBinContent(42,405.578441496);
  S11_PT_0->SetBinContent(43,320.689992811);
  S11_PT_0->SetBinContent(44,348.986195706);
  S11_PT_0->SetBinContent(45,286.105789272);
  S11_PT_0->SetBinContent(46,364.706277314);
  S11_PT_0->SetBinContent(47,286.105789272);
  S11_PT_0->SetBinContent(48,254.665586055);
  S11_PT_0->SetBinContent(49,267.241667342);
  S11_PT_0->SetBinContent(50,279.817748629);
  S11_PT_0->SetBinContent(51,204.361260909);
  S11_PT_0->SetBinContent(52,188.6411793);
  S11_PT_0->SetBinContent(53,169.77705737);
  S11_PT_0->SetBinContent(54,172.921097692);
  S11_PT_0->SetBinContent(55,141.480894475);
  S11_PT_0->SetBinContent(56,150.91293544);
  S11_PT_0->SetBinContent(57,188.6411793);
  S11_PT_0->SetBinContent(58,100.608610294);
  S11_PT_0->SetBinContent(59,116.328731902);
  S11_PT_0->SetBinContent(60,106.896650937);
  S11_PT_0->SetBinContent(61,100.608610294);
  S11_PT_0->SetBinContent(62,119.472732224);
  S11_PT_0->SetBinContent(63,97.4646099718);
  S11_PT_0->SetBinContent(64,81.7445283635);
  S11_PT_0->SetBinContent(65,91.1765693285);
  S11_PT_0->SetBinContent(66,78.6004880418);
  S11_PT_0->SetBinContent(67,62.8804064334);
  S11_PT_0->SetBinContent(68,59.7363661118);
  S11_PT_0->SetBinContent(69,72.3124473985);
  S11_PT_0->SetBinContent(70,81.7445283635);
  S11_PT_0->SetBinContent(71,40.8722441817);
  S11_PT_0->SetBinContent(72,25.1521585734);
  S11_PT_0->SetBinContent(73,50.3043251468);
  S11_PT_0->SetBinContent(74,50.3043251468);
  S11_PT_0->SetBinContent(75,25.1521585734);
  S11_PT_0->SetBinContent(76,37.7282358601);
  S11_PT_0->SetBinContent(77,28.296178895);
  S11_PT_0->SetBinContent(78,34.5842155384);
  S11_PT_0->SetBinContent(79,28.296178895);
  S11_PT_0->SetBinContent(80,18.86411793);
  S11_PT_0->SetBinContent(81,257.809626377); // overflow
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
