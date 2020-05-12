void selection_4()
{

  // ROOT version
  Int_t root_version = gROOT->GetVersionInt();

  // Creating a new TCanvas
  TCanvas* canvas = new TCanvas("canvas_plotflow_tempo9","canvas_plotflow_tempo9",0,0,700,500);
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
  TH1F* S5_ETA_0 = new TH1F("S5_ETA_0","S5_ETA_0",160,-8.0,8.0);
  // Content
  S5_ETA_0->SetBinContent(0,0.0); // underflow
  S5_ETA_0->SetBinContent(1,0.0);
  S5_ETA_0->SetBinContent(2,0.0);
  S5_ETA_0->SetBinContent(3,0.0);
  S5_ETA_0->SetBinContent(4,0.0);
  S5_ETA_0->SetBinContent(5,0.0);
  S5_ETA_0->SetBinContent(6,0.0);
  S5_ETA_0->SetBinContent(7,0.0);
  S5_ETA_0->SetBinContent(8,0.0);
  S5_ETA_0->SetBinContent(9,0.0);
  S5_ETA_0->SetBinContent(10,0.0);
  S5_ETA_0->SetBinContent(11,0.0);
  S5_ETA_0->SetBinContent(12,0.0);
  S5_ETA_0->SetBinContent(13,0.0);
  S5_ETA_0->SetBinContent(14,0.0);
  S5_ETA_0->SetBinContent(15,0.0);
  S5_ETA_0->SetBinContent(16,0.0);
  S5_ETA_0->SetBinContent(17,0.0);
  S5_ETA_0->SetBinContent(18,0.0);
  S5_ETA_0->SetBinContent(19,0.0);
  S5_ETA_0->SetBinContent(20,0.0);
  S5_ETA_0->SetBinContent(21,0.0);
  S5_ETA_0->SetBinContent(22,0.0);
  S5_ETA_0->SetBinContent(23,0.0);
  S5_ETA_0->SetBinContent(24,0.0);
  S5_ETA_0->SetBinContent(25,0.0);
  S5_ETA_0->SetBinContent(26,0.0);
  S5_ETA_0->SetBinContent(27,0.0);
  S5_ETA_0->SetBinContent(28,0.0);
  S5_ETA_0->SetBinContent(29,0.0);
  S5_ETA_0->SetBinContent(30,0.00232809093611);
  S5_ETA_0->SetBinContent(31,3.90354766587);
  S5_ETA_0->SetBinContent(32,4.71639890874);
  S5_ETA_0->SetBinContent(33,5.63547642905);
  S5_ETA_0->SetBinContent(34,6.5390757589);
  S5_ETA_0->SetBinContent(35,7.18934763897);
  S5_ETA_0->SetBinContent(36,8.09490972489);
  S5_ETA_0->SetBinContent(37,9.10002471761);
  S5_ETA_0->SetBinContent(38,10.1405932411);
  S5_ETA_0->SetBinContent(39,11.299278906);
  S5_ETA_0->SetBinContent(40,12.3605023391);
  S5_ETA_0->SetBinContent(41,13.6913588881);
  S5_ETA_0->SetBinContent(42,14.8293016991);
  S5_ETA_0->SetBinContent(43,16.4707534035);
  S5_ETA_0->SetBinContent(44,17.1044397949);
  S5_ETA_0->SetBinContent(45,18.8421984633);
  S5_ETA_0->SetBinContent(46,20.3840652812);
  S5_ETA_0->SetBinContent(47,22.1411157231);
  S5_ETA_0->SetBinContent(48,23.2279469269);
  S5_ETA_0->SetBinContent(49,24.7116945787);
  S5_ETA_0->SetBinContent(50,25.9752297936);
  S5_ETA_0->SetBinContent(51,26.9040811196);
  S5_ETA_0->SetBinContent(52,28.406221115);
  S5_ETA_0->SetBinContent(53,28.9656185881);
  S5_ETA_0->SetBinContent(54,30.3173499073);
  S5_ETA_0->SetBinContent(55,30.7578307458);
  S5_ETA_0->SetBinContent(56,31.6733505208);
  S5_ETA_0->SetBinContent(57,32.2547780321);
  S5_ETA_0->SetBinContent(58,32.6329023899);
  S5_ETA_0->SetBinContent(59,32.3426023721);
  S5_ETA_0->SetBinContent(60,32.8736618049);
  S5_ETA_0->SetBinContent(61,32.7392949619);
  S5_ETA_0->SetBinContent(62,32.4234471354);
  S5_ETA_0->SetBinContent(63,32.5469648541);
  S5_ETA_0->SetBinContent(64,32.0937360949);
  S5_ETA_0->SetBinContent(65,32.005843798);
  S5_ETA_0->SetBinContent(66,31.8921518521);
  S5_ETA_0->SetBinContent(67,31.2487076449);
  S5_ETA_0->SetBinContent(68,30.5171153029);
  S5_ETA_0->SetBinContent(69,30.0649698571);
  S5_ETA_0->SetBinContent(70,29.5533341143);
  S5_ETA_0->SetBinContent(71,28.8824353068);
  S5_ETA_0->SetBinContent(72,27.486983696);
  S5_ETA_0->SetBinContent(73,27.2293949469);
  S5_ETA_0->SetBinContent(74,27.1035507026);
  S5_ETA_0->SetBinContent(75,26.2518584759);
  S5_ETA_0->SetBinContent(76,25.3922512653);
  S5_ETA_0->SetBinContent(77,25.6501198371);
  S5_ETA_0->SetBinContent(78,25.0300807965);
  S5_ETA_0->SetBinContent(79,24.800378374);
  S5_ETA_0->SetBinContent(80,25.323051122);
  S5_ETA_0->SetBinContent(81,25.2204401533);
  S5_ETA_0->SetBinContent(82,25.0692959433);
  S5_ETA_0->SetBinContent(83,25.4065462057);
  S5_ETA_0->SetBinContent(84,25.6641749295);
  S5_ETA_0->SetBinContent(85,26.0166875191);
  S5_ETA_0->SetBinContent(86,26.6766532555);
  S5_ETA_0->SetBinContent(87,26.3950157477);
  S5_ETA_0->SetBinContent(88,27.4425518554);
  S5_ETA_0->SetBinContent(89,28.0764101378);
  S5_ETA_0->SetBinContent(90,28.3952760516);
  S5_ETA_0->SetBinContent(91,29.2284360235);
  S5_ETA_0->SetBinContent(92,29.9780409497);
  S5_ETA_0->SetBinContent(93,30.4240702717);
  S5_ETA_0->SetBinContent(94,31.1677949246);
  S5_ETA_0->SetBinContent(95,31.286811496);
  S5_ETA_0->SetBinContent(96,31.9944310311);
  S5_ETA_0->SetBinContent(97,32.6394742249);
  S5_ETA_0->SetBinContent(98,32.5473206287);
  S5_ETA_0->SetBinContent(99,32.4209647087);
  S5_ETA_0->SetBinContent(100,33.2105602902);
  S5_ETA_0->SetBinContent(101,33.0371342017);
  S5_ETA_0->SetBinContent(102,33.4243727832);
  S5_ETA_0->SetBinContent(103,32.1726181022);
  S5_ETA_0->SetBinContent(104,31.7039431323);
  S5_ETA_0->SetBinContent(105,31.4272265058);
  S5_ETA_0->SetBinContent(106,30.5075333756);
  S5_ETA_0->SetBinContent(107,29.746083956);
  S5_ETA_0->SetBinContent(108,29.4485685111);
  S5_ETA_0->SetBinContent(109,28.1252072119);
  S5_ETA_0->SetBinContent(110,27.105833256);
  S5_ETA_0->SetBinContent(111,25.6315276202);
  S5_ETA_0->SetBinContent(112,24.4179967143);
  S5_ETA_0->SetBinContent(113,23.0655258638);
  S5_ETA_0->SetBinContent(114,21.6515859702);
  S5_ETA_0->SetBinContent(115,20.6693085038);
  S5_ETA_0->SetBinContent(116,19.050310569);
  S5_ETA_0->SetBinContent(117,17.4295617438);
  S5_ETA_0->SetBinContent(118,16.075743747);
  S5_ETA_0->SetBinContent(119,14.8204193284);
  S5_ETA_0->SetBinContent(120,13.6630088554);
  S5_ETA_0->SetBinContent(121,12.4554941366);
  S5_ETA_0->SetBinContent(122,11.0509283021);
  S5_ETA_0->SetBinContent(123,10.0640897264);
  S5_ETA_0->SetBinContent(124,8.9331224945);
  S5_ETA_0->SetBinContent(125,8.04815935367);
  S5_ETA_0->SetBinContent(126,7.15432983205);
  S5_ETA_0->SetBinContent(127,6.1998787303);
  S5_ETA_0->SetBinContent(128,5.66602107091);
  S5_ETA_0->SetBinContent(129,4.48148778732);
  S5_ETA_0->SetBinContent(130,3.89884544598);
  S5_ETA_0->SetBinContent(131,0.0);
  S5_ETA_0->SetBinContent(132,0.0);
  S5_ETA_0->SetBinContent(133,0.0);
  S5_ETA_0->SetBinContent(134,0.0);
  S5_ETA_0->SetBinContent(135,0.0);
  S5_ETA_0->SetBinContent(136,0.0);
  S5_ETA_0->SetBinContent(137,0.0);
  S5_ETA_0->SetBinContent(138,0.0);
  S5_ETA_0->SetBinContent(139,0.0);
  S5_ETA_0->SetBinContent(140,0.0);
  S5_ETA_0->SetBinContent(141,0.0);
  S5_ETA_0->SetBinContent(142,0.0);
  S5_ETA_0->SetBinContent(143,0.0);
  S5_ETA_0->SetBinContent(144,0.0);
  S5_ETA_0->SetBinContent(145,0.0);
  S5_ETA_0->SetBinContent(146,0.0);
  S5_ETA_0->SetBinContent(147,0.0);
  S5_ETA_0->SetBinContent(148,0.0);
  S5_ETA_0->SetBinContent(149,0.0);
  S5_ETA_0->SetBinContent(150,0.0);
  S5_ETA_0->SetBinContent(151,0.0);
  S5_ETA_0->SetBinContent(152,0.0);
  S5_ETA_0->SetBinContent(153,0.0);
  S5_ETA_0->SetBinContent(154,0.0);
  S5_ETA_0->SetBinContent(155,0.0);
  S5_ETA_0->SetBinContent(156,0.0);
  S5_ETA_0->SetBinContent(157,0.0);
  S5_ETA_0->SetBinContent(158,0.0);
  S5_ETA_0->SetBinContent(159,0.0);
  S5_ETA_0->SetBinContent(160,0.0);
  S5_ETA_0->SetBinContent(161,0.0); // overflow
  S5_ETA_0->SetEntries(999999);
  // Style
  S5_ETA_0->SetLineColor(9);
  S5_ETA_0->SetLineStyle(1);
  S5_ETA_0->SetLineWidth(1);
  S5_ETA_0->SetFillColor(9);
  S5_ETA_0->SetFillStyle(1001);

  // Creating a new THStack
  THStack* stack = new THStack("mystack_10","mystack");
  stack->Add(S5_ETA_0);
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
  stack->GetXaxis()->SetTitle("#eta [ j_{2} ] ");

  // Finalizing the TCanvas
  canvas->SetLogx(0);
  canvas->SetLogy(0);

  // Saving the image
  canvas->SaveAs("../../HTML/MadAnalysis5job_0/selection_4.png");
  canvas->SaveAs("../../PDF/MadAnalysis5job_0/selection_4.png");
  canvas->SaveAs("../../DVI/MadAnalysis5job_0/selection_4.eps");

}
