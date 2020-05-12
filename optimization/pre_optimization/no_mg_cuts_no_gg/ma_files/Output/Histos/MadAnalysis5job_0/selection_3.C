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
  S4_PT_0->SetBinContent(3,289.77663575);
  S4_PT_0->SetBinContent(4,237.872529674);
  S4_PT_0->SetBinContent(5,201.147004261);
  S4_PT_0->SetBinContent(6,174.14383736);
  S4_PT_0->SetBinContent(7,154.194999819);
  S4_PT_0->SetBinContent(8,135.946484709);
  S4_PT_0->SetBinContent(9,120.303318475);
  S4_PT_0->SetBinContent(10,106.854041875);
  S4_PT_0->SetBinContent(11,94.346488464);
  S4_PT_0->SetBinContent(12,82.8104793424);
  S4_PT_0->SetBinContent(13,72.7969053864);
  S4_PT_0->SetBinContent(14,64.5072788888);
  S4_PT_0->SetBinContent(15,57.3839532548);
  S4_PT_0->SetBinContent(16,50.061034112);
  S4_PT_0->SetBinContent(17,45.1329972266);
  S4_PT_0->SetBinContent(18,40.2588062167);
  S4_PT_0->SetBinContent(19,35.5449775781);
  S4_PT_0->SetBinContent(20,32.1099824861);
  S4_PT_0->SetBinContent(21,28.5592807226);
  S4_PT_0->SetBinContent(22,25.4033727609);
  S4_PT_0->SetBinContent(23,23.0516311634);
  S4_PT_0->SetBinContent(24,20.5737734912);
  S4_PT_0->SetBinContent(25,18.4144899246);
  S4_PT_0->SetBinContent(26,17.0023848379);
  S4_PT_0->SetBinContent(27,15.318807795);
  S4_PT_0->SetBinContent(28,13.9491717938);
  S4_PT_0->SetBinContent(29,13.0869382293);
  S4_PT_0->SetBinContent(30,11.8170630053);
  S4_PT_0->SetBinContent(31,10.8606811068);
  S4_PT_0->SetBinContent(32,9.72972184561);
  S4_PT_0->SetBinContent(33,9.04914115964);
  S4_PT_0->SetBinContent(34,8.3945639941);
  S4_PT_0->SetBinContent(35,7.71658965637);
  S4_PT_0->SetBinContent(36,6.95693108556);
  S4_PT_0->SetBinContent(37,6.26068832534);
  S4_PT_0->SetBinContent(38,5.71224389879);
  S4_PT_0->SetBinContent(39,5.15033200717);
  S4_PT_0->SetBinContent(40,4.90196540805);
  S4_PT_0->SetBinContent(41,4.51191659921);
  S4_PT_0->SetBinContent(42,4.27048960216);
  S4_PT_0->SetBinContent(43,3.98457759722);
  S4_PT_0->SetBinContent(44,3.76871439926);
  S4_PT_0->SetBinContent(45,3.22976315646);
  S4_PT_0->SetBinContent(46,3.32504717078);
  S4_PT_0->SetBinContent(47,2.80981369698);
  S4_PT_0->SetBinContent(48,2.67979769386);
  S4_PT_0->SetBinContent(49,2.44770638038);
  S4_PT_0->SetBinContent(50,2.36173606356);
  S4_PT_0->SetBinContent(51,2.01554545984);
  S4_PT_0->SetBinContent(52,2.02247506824);
  S4_PT_0->SetBinContent(53,1.80423617586);
  S4_PT_0->SetBinContent(54,1.61860581802);
  S4_PT_0->SetBinContent(55,1.50464404063);
  S4_PT_0->SetBinContent(56,1.47908983546);
  S4_PT_0->SetBinContent(57,1.32370271114);
  S4_PT_0->SetBinContent(58,1.33285770921);
  S4_PT_0->SetBinContent(59,1.19810111042);
  S4_PT_0->SetBinContent(60,1.07034207696);
  S4_PT_0->SetBinContent(61,1.0679831719);
  S4_PT_0->SetBinContent(62,0.945035889025);
  S4_PT_0->SetBinContent(63,0.861384102856);
  S4_PT_0->SetBinContent(64,0.759305594514);
  S4_PT_0->SetBinContent(65,0.763972237057);
  S4_PT_0->SetBinContent(66,0.685055849856);
  S4_PT_0->SetBinContent(67,0.696549765654);
  S4_PT_0->SetBinContent(68,0.708279531983);
  S4_PT_0->SetBinContent(69,0.60846279026);
  S4_PT_0->SetBinContent(70,0.566639695403);
  S4_PT_0->SetBinContent(71,0.54331008041);
  S4_PT_0->SetBinContent(72,0.476007533006);
  S4_PT_0->SetBinContent(73,0.496922678155);
  S4_PT_0->SetBinContent(74,0.427295603907);
  S4_PT_0->SetBinContent(75,0.348281478647);
  S4_PT_0->SetBinContent(76,0.424987066929);
  S4_PT_0->SetBinContent(77,0.359879848248);
  S4_PT_0->SetBinContent(78,0.327454437663);
  S4_PT_0->SetBinContent(79,0.338967661224);
  S4_PT_0->SetBinContent(80,0.269395712041);
  S4_PT_0->SetBinContent(81,0.290315134479);
  S4_PT_0->SetBinContent(82,0.234563826545);
  S4_PT_0->SetBinContent(83,0.239200887834);
  S4_PT_0->SetBinContent(84,0.197349850685);
  S4_PT_0->SetBinContent(85,0.248417486869);
  S4_PT_0->SetBinContent(86,0.195107951475);
  S4_PT_0->SetBinContent(87,0.174125648887);
  S4_PT_0->SetBinContent(88,0.164922681214);
  S4_PT_0->SetBinContent(89,0.160197036064);
  S4_PT_0->SetBinContent(90,0.160215304487);
  S4_PT_0->SetBinContent(91,0.155572886592);
  S4_PT_0->SetBinContent(92,0.130014004384);
  S4_PT_0->SetBinContent(93,0.125342564882);
  S4_PT_0->SetBinContent(94,0.123060251284);
  S4_PT_0->SetBinContent(95,0.125415918394);
  S4_PT_0->SetBinContent(96,0.0998356497401);
  S4_PT_0->SetBinContent(97,0.109182646136);
  S4_PT_0->SetBinContent(98,0.10221050469);
  S4_PT_0->SetBinContent(99,0.0998554371999);
  S4_PT_0->SetBinContent(100,0.0882397185937);
  S4_PT_0->SetBinContent(101,1.35147231232); // overflow
  S4_PT_0->SetEntries(999999);
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
