#!/usr/bin/perl
&cetak_halaman;
sub cetak_halaman
{
print qq~
<html lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<meta http-equiv="Access-Control-Allow-Origin" content="*">
    <!-- Meta, title, CSS, favicons, etc. -->
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
	  
    <title>Walkthrough Master Area</title>

    <!-- Bootstrap -->
    <link href="/vendors/CMS/vendors/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Font Awesome -->
    <link href="/vendors/CMS/vendors/font-awesome/css/font-awesome.min.css" rel="stylesheet">
    <!-- NProgress -->
    <link href="/vendors/CMS/vendors/nprogress/nprogress.css" rel="stylesheet">
    <!-- iCheck -->
    <link href="/vendors/CMS/vendors/iCheck/skins/flat/green.css" rel="stylesheet">
    <!-- bootstrap-wysiwyg -->
    <link href="/vendors/CMS/vendors/google-code-prettify/bin/prettify.min.css" rel="stylesheet">
    <!-- Select2 -->
    <link href="/vendors/CMS/vendors/select2/dist/css/select2.min.css" rel="stylesheet">
    <!-- Switchery -->
    <link href="/vendors/CMS/vendors/switchery/dist/switchery.min.css" rel="stylesheet">
    <!-- starrr -->
    <link href="/vendors/CMS/vendors/starrr/dist/starrr.css" rel="stylesheet">
    <!-- bootstrap-daterangepicker -->
    <link href="/vendors/CMS/vendors/bootstrap-daterangepicker/daterangepicker.css" rel="stylesheet">

    <!-- Custom Theme Style -->
    <link href="/vendors/CMS/build/css/custom.min.css" rel="stylesheet">
	
	<style>
	.selected {
		background-color: #FFCF8B !important;
	}
	</style>
  </head>
  
  <div id="viewMasterAreaModal" class="modal fade" role="dialog">
		<div class="modal-dialog">
			<!-- Modal content-->
			<div class="modal-content">
				<div class="modal-header">
					<button type="button" class="close" data-dismiss="modal">&times;</button>
					<h4 class="modal-title">Lihat Data Master Area</h4>
				</div>
				<div class="modal-body">
					<table width="100%" style="margin-top:20px;">
						<tr>
							<td width="30%" style="padding:10px;">Area BU</td>
							<td width="70%" id="" colspan="3"><input type="text" id="viewAreaBU" name="viewAreaBU" class="form-control" style="display:inline;" disabled/><br/></td>
						</tr>
						<tr>
							<td width="30%" style="padding:10px;">Area Div</td>
							<td width="70%" id="" colspan="3"><input type="text" id="viewAreaDiv" name="viewAreaDiv" class="form-control" style="display:inline;" disabled/><br/></td>
						</tr>
						<tr>
							<td width="30%" style="padding:10px;">Wilayah</td>
							<td width="70%" id="" colspan="3"><input type="text" id="viewAreaWilayah" name="viewAreaWilayah" class="form-control" style="display:inline;" disabled/><br/></td>
						</tr>
						<tr>
							<td width="30%" style="padding:10px;">Lokasi</td>
							<td width="70%" id="" colspan="3"><input type="text" id="viewAreaLokasi" name="viewAreaLokasi" class="form-control" style="display:inline;" disabled/><br/></td>
						</tr>
						<tr>
							<td width="30%" style="padding:10px;">Free Standing</td>
							<td width="70%" id="" colspan="3"><input type="text" id="viewIsfstand" name="viewIsfstand" class="form-control" style="display:inline;" disabled/><br/></td>
						</tr>
					</table>
				</div>
				<div class="modal-footer">
					<button type="button" class="btn btn-default" data-dismiss="modal"><i class="glyphicon glyphicon-remove"></i> Tutup</button>
				</div>
			</div>
		</div>
	</div>
  
  <div id="addMasterAreaModal" class="modal fade" role="dialog">
		<div class="modal-dialog">
			<!-- Modal content-->
			<div class="modal-content">
				<div class="modal-header">
					<button type="button" class="close" data-dismiss="modal">&times;</button>
					<h4 class="modal-title">Tambah Data Master Area</h4>
				</div>
				<div class="modal-body">
					<table width="100%" style="margin-top:20px;">
						<tr>
							<td width="30%" style="padding:10px;">Area BU</td>
							<td width="70%" id="" colspan="3"><select id="addAreaBU" class="form-control" style="display:inline;"></select><br/></td>
						</tr>
						<tr>
							<td width="30%" style="padding:10px;">Area Div</td>
							<td width="70%" id="" colspan="3"><select id="addAreaDiv" class="form-control" style="display:inline;"></select><br/></td>
						</tr>
						<tr>
							<td width="30%" style="padding:10px;">Wilayah</td>
							<td width="70%" id="" colspan="3"><input type="text" id="addAreaWilayah" name="addAreaWilayah" class="form-control" style="display:inline;" maxlength="30"/><br/></td>
						</tr>
						<tr>
							<td width="30%" style="padding:10px;">Lokasi</td>
							<td width="70%" id="" colspan="3"><input type="text" id="addAreaLokasi" name="addAreaLokasi" class="form-control" style="display:inline;" maxlength="20"/><br/></td>
						</tr>
						<tr>
							<td width="30%" style="padding:10px;">Free Standing</td>
							<td width="70%" id="" colspan="3"><select id="addIsfstand" class="form-control" style="display:inline;"><option value="Y">Ya</option><option value="N">Tidak</option></select></td>
						</tr>
					</table>
				</div>
				<div class="modal-footer">
					<button type="button" class="btn btn-success" data-dismiss="modal" id="confirmAddAreaModal"><i class="glyphicon glyphicon-ok"></i> Tambah Area</button>
					<button type="button" class="btn btn-default" data-dismiss="modal"><i class="glyphicon glyphicon-remove"></i> Tutup</button>
				</div>
			</div>
		</div>
	</div>
	
	<div id="editMasterAreaModal" class="modal fade" role="dialog">
		<div class="modal-dialog">
			<!-- Modal content-->
			<div class="modal-content">
				<div class="modal-header">
					<button type="button" class="close" data-dismiss="modal">&times;</button>
					<h4 class="modal-title">Ubah Data Master Area</h4>
				</div>
				<div class="modal-body">
					<table width="100%" style="margin-top:20px;">
						<tr>
							<td width="30%" style="padding:10px;">Area BU</td>
							<td width="70%" id="" colspan="3"><select id="editAreaBU" class="form-control" style="display:inline;"></select><br/></td>
						</tr>
						<tr>
							<td width="30%" style="padding:10px;">Area Div</td>
							<td width="70%" id="" colspan="3"><select id="editAreaDiv" class="form-control" style="display:inline;"></select><br/></td>
						</tr>
						<tr>
							<td width="30%" style="padding:10px;">Wilayah</td>
							<td width="70%" id="" colspan="3"><input type="text" id="editAreaWilayah" name="editAreaWilayah" class="form-control" style="display:inline;" maxlength="30"/><br/></td>
						</tr>
						<tr>
							<td width="30%" style="padding:10px;">Lokasi</td>
							<td width="70%" id="" colspan="3"><input type="text" id="editAreaLokasi" name="editAreaLokasi" class="form-control" style="display:inline;" maxlength="20"/><br/></td>
						</tr>
						<tr>
							<td width="30%" style="padding:10px;">Free Standing</td>
							<td width="70%" id="" colspan="3"><select id="editIsfstand" class="form-control" style="display:inline;"><option value="Y">Ya</option><option value="N">Tidak</option></select><br/></td>
						</tr>
					</table>
				</div>
				<div class="modal-footer">
					<button type="button" class="btn btn-info" data-dismiss="modal" id="confirmEditAreaModal"><i class="glyphicon glyphicon-ok"></i> Ubah Informasi Area</button>
					<button type="button" class="btn btn-default" data-dismiss="modal"><i class="glyphicon glyphicon-remove"></i> Tutup</button>
				</div>
			</div>
		</div>
	</div>
	
	<div id="deleteMasterAreaModal" class="modal fade" role="dialog">
		<div class="modal-dialog">
			<!-- Modal content-->
			<div class="modal-content">
				<div class="modal-header">
					<button type="button" class="close" data-dismiss="modal">&times;</button>
					<h4 class="modal-title">Hapus Data Master Area</h4>
				</div>
				<div class="modal-body">
					Hapus Area ini?
					<table width="100%" style="margin-top:20px;">
						<tr>
							<td width="30%" style="padding:10px;">Area BU</td>
							<td width="70%" id="" colspan="3"><input type="text" id="deleteAreaBU" name="deleteAreaBU" class="form-control" style="display:inline;" disabled/><br/></td>
						</tr>
						<tr>
							<td width="30%" style="padding:10px;">Area Div</td>
							<td width="70%" id="" colspan="3"><input type="text" id="deleteAreaDiv" name="deleteAreaDiv" class="form-control" style="display:inline;" disabled/><br/></td>
						</tr>
						<tr>
							<td width="30%" style="padding:10px;">Wilayah</td>
							<td width="70%" id="" colspan="3"><input type="text" id="deleteAreaWilayah" name="deleteAreaWilayah" class="form-control" style="display:inline;" disabled/><br/></td>
						</tr>
						<tr>
							<td width="30%" style="padding:10px;">Lokasi</td>
							<td width="70%" id="" colspan="3"><input type="text" id="deleteAreaLokasi" name="deleteAreaLokasi" class="form-control" style="display:inline;" disabled/><br/></td>
						</tr>
						<tr>
							<td width="30%" style="padding:10px;">Free Standing</td>
							<td width="70%" id="" colspan="3"><input type="text" id="deleteIsfstand" name="deleteIsfstand" class="form-control" style="display:inline;" disabled/><br/></td>
						</tr>
					</table>
				</div>
				<div class="modal-footer">
					<button type="button" class="btn btn-danger" data-dismiss="modal" id="confirmDeleteAreaModal"><i class="glyphicon glyphicon-ok"></i> Hapus Informasi Area</button>
					<button type="button" class="btn btn-default" data-dismiss="modal"><i class="glyphicon glyphicon-remove"></i> Tutup</button>
				</div>
			</div>
		</div>
	</div>

  <body class="nav-md">
    <div class="container body">
      <div class="main_container">
        <div class="col-md-3 left_col">
          <div class="left_col scroll-view">
            <div class="navbar nav_title" style="border: 0;">
              <a href="controlPanel.cgi" class="site_title"><i class="fa fa-cog"></i> <span>WALKTHROUGH CP</span></a>
            </div>

            <div class="clearfix"></div>

           <!-- menu profile quick info -->
            <div class="profile clearfix">
				<div class="profile_pic">
					<img src="/vendors/CMS/images/img.jpg" alt="..." class="img-circle profile_img">
				</div>
				<div class="profile_info">
					<span>Welcome,</span>
					<h2>Administrator</h2>
				</div>
            </div>
            <!-- /menu profile quick info -->

            <br />

            <!-- sidebar menu -->
            <div id="sidebar-menu" class="main_menu_side hidden-print main_menu">
				<div class="menu_section">
					<h3>General</h3>
					<ul class="nav side-menu">
						<li><a><i class="fa fa-home"></i> Home <span class="fa fa-chevron-down"></span></a>
						<ul class="nav child_menu">
							<li><a href="controlPanel.cgi">Dashboard</a></li>
						</ul>
					</li>
                  <li><a><i class="fa fa-qrcode"></i> Masters <span class="fa fa-chevron-down"></span></a>
                    <ul class="nav child_menu">
					  <li><a href="walkthroughMasterBrand.cgi">Master Brand</a></li>
					  <li><a href="walkthroughMasterCabang.cgi">Master Cabang</a></li>
					  <li><a href="walkthroughMasterCabangType.cgi">Master Tipe Cabang</a></li>
					  <li><a href="walkthroughMasterDeviceValidation.cgi">Master Device Validate</a></li>
                    </ul>
                  </li>
				  <li><a><i class="fa fa-desktop"></i> Walkthrough <span class="fa fa-chevron-down"></span></a>
                    <ul class="nav child_menu">
                      <li><a href="walkthroughMasterActivities.cgi">Master Activities</a></li>
					  <li><a href="walkthroughMasterArea.cgi">Master Area</a></li>
					  <li><a href="walkthroughMasterChecklist.cgi">Master Checklist</a></li>
					  <li><a href="walkthroughMasterDiv.cgi">Master Div</a></li>
					  <li><a href="walkthroughMasterLogin.cgi">Master Login</a></li>
					  <li><a href="walkthroughMasterObject.cgi">Master Object</a></li>
					  <li><a href="walkthroughMasterUser.cgi">Master User</a></li>
					  <li><a href="walkthroughMasterCheck.cgi">Master Check</a></li>
                    </ul>
                  </li>
				  <li><a><i class="fa fa-cogs"></i> System Config <span class="fa fa-chevron-down"></span></a>
						<ul class="nav child_menu">
							<li><a href="pageGeneralConfig.cgi">General Configuration</a></li>
							<li><a href="pageAdvancedConfig.cgi">Advanced Configuration</a></li>
						</ul>
					</li>
                </ul>
              </div>
              <div class="menu_section">
                <h3>Inquiry</h3>
                <ul class="nav side-menu">
                  <li><a><i class="fa fa-code"></i> Development Inquiry <span class="fa fa-chevron-down"></span></a>
                    <ul class="nav child_menu">
                        <li><a href="#level1_1">Level One</a>
                        <li><a>Development<span class="fa fa-chevron-down"></span></a>
                          <ul class="nav child_menu">
                            <li class="sub_menu"><a href="level2.html">Developers</a>
                            </li>
                            <li><a href="#level2_1">Level Two</a>
                            </li>
                            <li><a href="#level2_2">Level Two</a>
                            </li>
                          </ul>
                        </li>
                        <li><a href="#level1_2">Level One</a>
                        </li>
                    </ul>
                  </li>                  
                </ul>
              </div>
            </div>
            <!-- /sidebar menu -->

            <!-- /menu footer buttons -->
            <div class="sidebar-footer hidden-small">
              <a data-toggle="tooltip" data-placement="top" title="Settings">
                <span class="glyphicon glyphicon-cog" aria-hidden="true"></span>
              </a>
              <a data-toggle="tooltip" data-placement="top" title="FullScreen">
                <span class="glyphicon glyphicon-fullscreen" aria-hidden="true"></span>
              </a>
              <a data-toggle="tooltip" data-placement="top" title="Lock">
                <span class="glyphicon glyphicon-eye-close" aria-hidden="true"></span>
              </a>
              <a data-toggle="tooltip" data-placement="top" title="Logout" href="login.html">
                <span class="glyphicon glyphicon-off" aria-hidden="true"></span>
              </a>
            </div>
            <!-- /menu footer buttons -->
          </div>
        </div>

        <!-- top navigation -->
        <div class="top_nav">
          <div class="nav_menu">
            <nav>
              <div class="nav toggle">
                <a id="menu_toggle"><i class="fa fa-bars"></i></a>
              </div>

              <ul class="nav navbar-nav navbar-right">
                <li class="">
                  <a href="javascript:;" class="user-profile dropdown-toggle" data-toggle="dropdown" aria-expanded="false">
                    <img src="/vendors/CMS/images/img.jpg" alt="">Administrator
                    <span class=" fa fa-angle-down"></span>
                  </a>
                  <ul class="dropdown-menu dropdown-usermenu pull-right">
                    <li><a href="javascript:;"> Profile</a></li>
                    <li>
                      <a href="javascript:;">
                        <span class="badge bg-red pull-right">50%</span>
                        <span>Settings</span>
                      </a>
                    </li>
                    <li><a href="javascript:;">Help</a></li>
                    <li><a href="login.html"><i class="fa fa-sign-out pull-right"></i> Log Out</a></li>
                  </ul>
                </li>

                <li role="presentation" class="dropdown">
                  <a href="javascript:;" class="dropdown-toggle info-number" data-toggle="dropdown" aria-expanded="false">
                    <i class="fa fa-envelope-o"></i>
                    <span class="badge bg-green">6</span>
                  </a>
                  <ul id="menu1" class="dropdown-menu list-unstyled msg_list" role="menu">
                    <li>
                      <a>
                        <span class="image"><img src="/vendors/CMS/images/img.jpg" alt="Profile Image" /></span>
                        <span>
                          <span>John Smith</span>
                          <span class="time">3 mins ago</span>
                        </span>
                        <span class="message">
                          Film festivals used to be do-or-die moments for movie makers. They were where...
                        </span>
                      </a>
                    </li>
                    <li>
                      <a>
                        <span class="image"><img src="/vendors/CMS/images/img.jpg" alt="Profile Image" /></span>
                        <span>
                          <span>John Smith</span>
                          <span class="time">3 mins ago</span>
                        </span>
                        <span class="message">
                          Film festivals used to be do-or-die moments for movie makers. They were where...
                        </span>
                      </a>
                    </li>
                    <li>
                      <a>
                        <span class="image"><img src="/vendors/CMS/images/img.jpg" alt="Profile Image" /></span>
                        <span>
                          <span>John Smith</span>
                          <span class="time">3 mins ago</span>
                        </span>
                        <span class="message">
                          Film festivals used to be do-or-die moments for movie makers. They were where...
                        </span>
                      </a>
                    </li>
                    <li>
                      <a>
                        <span class="image"><img src="/vendors/CMS/images/img.jpg" alt="Profile Image" /></span>
                        <span>
                          <span>John Smith</span>
                          <span class="time">3 mins ago</span>
                        </span>
                        <span class="message">
                          Film festivals used to be do-or-die moments for movie makers. They were where...
                        </span>
                      </a>
                    </li>
                    <li>
                      <div class="text-center">
                        <a>
                          <strong>See All Alerts</strong>
                          <i class="fa fa-angle-right"></i>
                        </a>
                      </div>
                    </li>
                  </ul>
                </li>
              </ul>
            </nav>
          </div>
        </div>
        <!-- /top navigation -->

        <!-- page content -->
        <div class="right_col" role="main">
          <div class="">
            <div class="page-title">
              <div class="title_left">
                <h3>Walkthrough Master Area</h3>
              </div>

              <div class="title_right">
                <div class="col-md-5 col-sm-5 col-xs-12 form-group pull-right top_search">
                  <div class="input-group">
                      
                  </div>
                </div>
              </div>
            </div>
            <div class="clearfix"></div>

			  <div class="col-md-12 col-sm-12 col-xs-12">
              <div class="x_panel">
                <div class="x_title">
                  <h2>List Area<small>Walkthrough Area listing for Sarirasa Nusantara</small><small style="color:green;"><i class="fa fa-cog"></i> CORE, Tested.</small></h2>
                  <div class="clearfix"></div>
                </div>
				<button style="width:25%" class="btn btn-success form-control" data-toggle="modal" data-target="#addMasterAreaModal" type="button" id="openModalAddMasterArea"><i class="fa fa-plus"></i> Tambah Master Area</button>
                <div class="x_content">
                  <div id="alerts"></div>
					<table id="tableMasterArea" width="100%"></table>
                  <br />

                  <div class="ln_solid"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

        <!-- footer content -->
        <footer>
          <div class="pull-right">
            &copy; 2018. MIS Department - Sarirasa Group, Indonesia. Developed by : MIS TEAM</a>.
          </div>
          <div class="clearfix"></div>
        </footer>
        <!-- /footer content -->
      </div>
    </div>

    <!-- jQuery -->
    <script src="/vendors/CMS/vendors/jquery/dist/jquery.min.js"></script>
    <!-- Bootstrap -->
    <script src="/vendors/CMS/vendors/bootstrap/dist/js/bootstrap.min.js"></script>
    <!-- FastClick -->
    <script src="/vendors/CMS/vendors/fastclick/lib/fastclick.js"></script>
    <!-- NProgress -->
    <script src="/vendors/CMS/vendors/nprogress/nprogress.js"></script>
    <!-- bootstrap-progressbar -->
    <script src="/vendors/CMS/vendors/bootstrap-progressbar/bootstrap-progressbar.min.js"></script>
    <!-- iCheck -->
    <script src="/vendors/CMS/vendors/iCheck/icheck.min.js"></script>
    <!-- bootstrap-daterangepicker -->
    <script src="/vendors/CMS/vendors/moment/min/moment.min.js"></script>
    <script src="/vendors/CMS/vendors/bootstrap-daterangepicker/daterangepicker.js"></script>
    <!-- bootstrap-wysiwyg -->
    <script src="/vendors/CMS/vendors/bootstrap-wysiwyg/js/bootstrap-wysiwyg.min.js"></script>
    <script src="/vendors/CMS/vendors/jquery.hotkeys/jquery.hotkeys.js"></script>
    <script src="/vendors/CMS/vendors/google-code-prettify/src/prettify.js"></script>
    <!-- jQuery Tags Input -->
    <script src="/vendors/CMS/vendors/jquery.tagsinput/src/jquery.tagsinput.js"></script>
    <!-- Switchery -->
    <script src="/vendors/CMS/vendors/switchery/dist/switchery.min.js"></script>
    <!-- Select2 -->
    <script src="/vendors/CMS/vendors/select2/dist/js/select2.full.min.js"></script>
    <!-- Parsley -->
    <script src="/vendors/CMS/vendors/parsleyjs/dist/parsley.min.js"></script>
    <!-- Autosize -->
    <script src="/vendors/CMS/vendors/autosize/dist/autosize.min.js"></script>
    <!-- jQuery autocomplete -->
    <script src="/vendors/CMS/vendors/devbridge-autocomplete/dist/jquery.autocomplete.min.js"></script>
    <!-- starrr -->
    <script src="/vendors/CMS/vendors/starrr/dist/starrr.js"></script>
    <!-- Custom Theme Scripts -->
    <script src="/vendors/CMS/build/js/custom.min.js"></script>
	
	<!-- load jquery data-tables per-halaman yang menggunakan -->
	<script type="text/javascript" src="/vendors/jquery.dataTables.min.js"></script>
	<script type="text/javascript" src="/vendors/dataTables.bootstrap.min.js"></script>

	<!-- load notify.js per-halaman yang menggunakan -->
	<script src="/vendors/notifyjs/notify.min.js"></script>
	
	<script type="text/javascript">
		var globalVar = {};
		globalVar['viewRecid'] = '';
		globalVar['updateRecid'] = '';
		globalVar['deleteRecid'] = '';
		
		\$(document).ready(function(){
			getLoadComponentsBU();
			getLoadComponentsDIV();
			initAreaMaster();
			
			\$('#tableMasterArea').on('click', '.clickableTableMasterArea', function(){
				var recidVal = \$(this).data('recid');
				var areaBUVal = \$(this).data('areabu');
				var areaDivVal = \$(this).data('areadiv');
				var areaWilayahVal = \$(this).data('wilayah');
				var areaLokasiVal = \$(this).data('lokasi');
				var areaIsfstandVal = \$(this).data('isfstand');
				
				globalVar['viewRecid'] = recidVal;
				globalVar['updateRecid'] = recidVal;
				globalVar['deleteRecid'] = recidVal;
				
				\$('#viewAreaBU').val(areaBUVal);
				\$('#viewAreaDiv').val(areaDivVal);
				\$('#viewAreaWilayah').val(areaWilayahVal);
				\$('#viewAreaLokasi').val(areaLokasiVal);
				\$('#viewIsfstand').val(areaIsfstandVal);
				
				\$('#editAreaBU option[value='+areaBUVal+']').prop("selected",true);
				\$('#editAreaDiv option[value='+areaDivVal+']').prop("selected",true);
				\$('#editAreaWilayah').val(areaWilayahVal);
				\$('#editAreaLokasi').val(areaLokasiVal);
				\$('#editIsfstand').val(areaIsfstandVal);
				
				\$('#deleteAreaBU').val(recidVal);
				\$('#deleteAreaDiv').val(areaBUVal);
				\$('#deleteAreaWilayah').val(areaDivVal);
				\$('#deleteAreaLokasi').val(areaLokasiVal);
				\$('#deleteIsfstand').val(areaIsfstandVal);
				
				\$(this).addClass("selected").siblings().removeClass("selected");
			});
			
			\$('#confirmAddAreaModal').on('click', function(){
				addAreaFunction();
			});
			
			\$('#confirmEditAreaModal').on('click', function(){
				editAreaFunction();
			});
			
			\$('#confirmDeleteAreaModal').on('click', function(){
				deleteAreaFunction();
			});
		});
		
		// load components for BU and DIV
		
		function getLoadComponentsBU(){
			\$.ajax({
				url 		: 'http://172.25.2.149:8080/cabangtype/getallcabangtype',
				type 		: 'GET',
				success		: function(response) {buComponentsResult(response)},
				error		: function(e) {onError(e)}
			});
		}
		
		function buComponentsResult(response){
			var selectAddBu = '<select id="addAreaBu" class="form-control" style="display:inline;">';
			var selectEditBu = '<select id="editAreaBu" class="form-control" style="display:inline;">';
			for(var ix = 0; ix < response.DATA_MASTER_CABANG_TYPE.length; ix++){
				selectAddBu += '<option value="'+response.DATA_MASTER_CABANG_TYPE[ix].TYPE_BU+'">'+response.DATA_MASTER_CABANG_TYPE[ix].TYPE_BU+'</option>';
				selectEditBu += '<option value="'+response.DATA_MASTER_CABANG_TYPE[ix].TYPE_BU+'">'+response.DATA_MASTER_CABANG_TYPE[ix].TYPE_BU+'</option>';
			}
			selectAddBu += '</select>';
			selectEditBu += '</select>';
			
			\$('#addAreaBU').html(selectAddBu);
			\$('#editAreaBU').html(selectEditBu);
		}
		
		function getLoadComponentsDIV(){
			\$.ajax({
				url 		: 'http://172.25.2.149:8080/div/getalldiv',
				type 		: 'GET',
				success		: function(response) {divComponentsResult(response)},
				error		: function(e) {onError(e)}
			});
		}
		
		function divComponentsResult(response){
			var selectAddDiv = '<select id="addAreaDiv" class="form-control" style="display:inline;">';
			var selectEditDiv = '<select id="editAreaDiv" class="form-control" style="display:inline;">';
			for(var ix = 0; ix < response.DATA_MASTER_WALKTHROUGH_DIV.length; ix++){
				selectAddDiv += '<option value="'+response.DATA_MASTER_WALKTHROUGH_DIV[ix].DIV_ID+'">'+response.DATA_MASTER_WALKTHROUGH_DIV[ix].DIV_ID+'</option>';
				selectEditDiv += '<option value="'+response.DATA_MASTER_WALKTHROUGH_DIV[ix].DIV_ID+'">'+response.DATA_MASTER_WALKTHROUGH_DIV[ix].DIV_ID+'</option>';
			}
			selectAddDiv += '</select>';
			selectEditDiv += '</select>';
			
			\$('#addAreaDiv').html(selectAddDiv);
			\$('#editAreaDiv').html(selectEditDiv);
		}
		
		// view / get data master area
		function initAreaMaster(){
			\$.ajax({
				url 		: 'http://172.25.2.149:8080/area/getallarea',
				type 		: 'GET',
				success		: function(response) {areaMasterResult(response)},
				error		: function(e) {onError(e)}
			});
		}

		function areaMasterResult(response){
			var htmlTables = '	<thead> \\
									<tr style="color: #FFFFFF; background-color:#800000; text-align:center;" height=30> \\
										<td>No</td> \\
										<td>BU</td> \\
										<td>Div</td> \\
										<td>Wilayah</td> \\
										<td>Lokasi</td> \\
										<td>Free Standing</td> \\
										<td>ACTION</td> \\
									</tr> \\
								</thead>';
			for(var ix = 0; ix < response.DATA_MASTER_WALKTHROUGH_AREA.length; ix++){ 
				htmlTables += '	<tr style="background:#EEEEEE; cursor:pointer; text-align:center; border-bottom: solid #CCCCCC;" \\
								data-recid = "'+response.DATA_MASTER_WALKTHROUGH_AREA[ix].RECID+'" \\
								data-areabu = "'+response.DATA_MASTER_WALKTHROUGH_AREA[ix].AREA_BU+'" \\
								data-areadiv = "'+response.DATA_MASTER_WALKTHROUGH_AREA[ix].AREA_DIV+'" \\
								data-wilayah = "'+response.DATA_MASTER_WALKTHROUGH_AREA[ix].WILAYAH+'" \\
								data-lokasi = "'+response.DATA_MASTER_WALKTHROUGH_AREA[ix].LOKASI+'" \\
								data-isfstand = "'+response.DATA_MASTER_WALKTHROUGH_AREA[ix].ISFSTAND_ONLY+'" \\
								cellspacing="1" cellpadding="1" class="huruf2 clickableTableMasterArea"> \\
									<td>'+(ix+1)+'</td> \\
									<td>'+response.DATA_MASTER_WALKTHROUGH_AREA[ix].AREA_BU+'</td> \\
									<td>'+response.DATA_MASTER_WALKTHROUGH_AREA[ix].AREA_DIV+'</td> \\
									<td>'+response.DATA_MASTER_WALKTHROUGH_AREA[ix].WILAYAH+'</td> \\
									<td>'+response.DATA_MASTER_WALKTHROUGH_AREA[ix].LOKASI+'</td> \\
									<td>'+response.DATA_MASTER_WALKTHROUGH_AREA[ix].ISFSTAND_ONLY+'</td> \\
									<td id="EDIT" style="padding:3px; text-align:center; border-bottom: solid #CCCCCC;" >\\
										<button id="openModalViewMasterAreaButton" class="btn btn-md btn-success" data-toggle="modal" data-target="#viewMasterAreaModal" title="VIEW !"><i class="glyphicon glyphicon-search"></i></button> \\
										<button id="openModalEditMasterAreaButton" class="btn btn-md btn-primary" data-toggle="modal" data-target="#editMasterAreaModal" title="EDIT !"><i class="glyphicon glyphicon-pencil"></i></button> \\
										<button id="openModalDeleteMasterAreaButton" class="btn btn-md btn-danger" data-toggle="modal" data-target="#deleteMasterAreaModal" title="DELETE !"><i class="glyphicon glyphicon-remove"></i></button> \\
									</td> \\
								</tr>';
			}
			htmlTables += '	<tfoot>\\
								<tr style="color: #FFFFFF; background-color:#800000; text-align:center;" height=30> \\
									<td>No</td> \\
									<td>BU</td> \\
									<td>Div</td> \\
									<td>Wilayah</td> \\
									<td>Lokasi</td> \\
									<td>Free Standing</td> \\
									<td>ACTION</td> \\
								</tr> \\
							</tfoot>';
			\$('#tableMasterArea').html(htmlTables);
			\$('#tableMasterArea').dataTable().fnDestroy();
			\$('#tableMasterArea').dataTable({fixedHeader: true, "lengthMenu": [[25, 50, 100], [25, 50, 100]],dom: "<'row'<'col-sm-4'l><'col-sm-4'p><'col-sm-4'f>><'row'<'col-sm-12'tr>><'row'<'col-sm-4'i><'col-sm-4'p><'col-sm-4'f>>"});
		}
		
		// add master area		
		function addAreaFunction(){
			\$.ajax({
                url			: 'http://172.25.2.149:8080/area/addarea',
                type		: 'POST',
                contentType	: 'application/x-www-form-urlencoded',
                data		: getDataAddMasterArea(),
                success		: function(response) {addMasterAreaResult(response)},
				error		: function(e) {onError(e)}
            });
		}
		
		function getDataAddMasterArea(){
			var strUrlEncoded = "";
				
				strUrlEncoded = 'addAreaBU='+\$('#addAreaBU').val()+
								'&addAreaDiv='+\$('#addAreaDiv').val()+
								'&addAreaWilayah='+\$('#addAreaWilayah').val()+
								'&addAreaLokasi='+\$('#addAreaLokasi').val()+
								'&addIsfstand='+\$('#addIsfstand').val();
				
			return strUrlEncoded;
		}
		
		function addMasterAreaResult(response){
			var result = \$.parseJSON(response.jsonResponse);
			if(result.DATA_MASTER_WALKTHROUGH_AREA[0].RESULT == true){
				\$.notify('SUKSES !\\n\\nSukses menambahkan data master area :\\n \\
					Status : '+result.DATA_MASTER_WALKTHROUGH_AREA[0].RESULT+'\\n \\
					Function : '+result.DATA_MASTER_WALKTHROUGH_AREA[0].MESSAGE+'\\n \\
					', "success");

				initAreaMaster();
			} else {
				\$.notify('GAGAL !\\n\\nGagal menambahkan data master area :\\n \\
					Status : '+result.DATA_MASTER_WALKTHROUGH_AREA[0].RESULT+'\\n \\
					Function : '+result.DATA_MASTER_WALKTHROUGH_AREA[0].MESSAGE+'\\n \\
					', "error");

				initAreaMaster();
			}
		}
		
		// edit master area		
		function editAreaFunction(){
			\$.ajax({
                url			: 'http://172.25.2.149:8080/area/editarea',
                type		: 'POST',
                contentType	: 'application/x-www-form-urlencoded',
                data		: getDataEditMasterArea(),
                success		: function(response) {editAreaMasterResult(response)},
				error		: function(e) {onError(e)}
            });
		}
		
		function getDataEditMasterArea(){
			var strUrlEncoded = "";
				
				strUrlEncoded = 'recid='+globalVar['updateRecid']+
								'&editAreaBU='+\$('#editAreaBU').val()+
								'&editAreaDiv='+\$('#editAreaDiv').val()+
								'&editAreaWilayah='+\$('#editAreaWilayah').val()+
								'&editAreaLokasi='+\$('#editAreaLokasi').val()+
								'&editIsfstand='+\$('#editIsfstand').val();
				
			return strUrlEncoded;
		}
		
		function editAreaMasterResult(response){
			var result = \$.parseJSON(response.jsonResponse);
			if(result.DATA_MASTER_WALKTHROUGH_AREA[0].RESULT == true){
				\$.notify('SUKSES !\\n\\nSukses mengubah data master area :\\n \\
					Status : '+result.DATA_MASTER_WALKTHROUGH_AREA[0].RESULT+'\\n \\
					Function : '+result.DATA_MASTER_WALKTHROUGH_AREA[0].MESSAGE+'\\n \\
					', "success");

				initAreaMaster();
			} else {
				\$.notify('GAGAL !\\n\\nSukses mengubah data master area :\\n \\
					Status : '+result.DATA_MASTER_WALKTHROUGH_AREA[0].RESULT+'\\n \\
					Function : '+result.DATA_MASTER_WALKTHROUGH_AREA[0].MESSAGE+'\\n \\
					', "error");

				initAreaMaster();
			}
		}
		
		// delete master area	
		function deleteAreaFunction(){
			\$.ajax({
                url			: 'http://172.25.2.149:8080/area/deletearea',
                type		: 'POST',
                contentType	: 'application/x-www-form-urlencoded',
                data		: getDataMasterArea(),
                success		: function(response) {deleteAreaMasterResult(response)},
				error		: function(e) {onError(e)}
            });
		}
		
		function getDataMasterArea(){
			var strUrlEncoded = "";
			
				strUrlEncoded = 'recid='+globalVar['updateRecid'];
				
			return strUrlEncoded;
		}
		
		function deleteAreaMasterResult(response){
			var result = \$.parseJSON(response.jsonResponse);
			if(result.DATA_MASTER_WALKTHROUGH_AREA[0].RESULT == true){
				\$.notify('SUKSES !\\n\\nSukses menghapus data master area :\\n \\
					Status : '+result.DATA_MASTER_WALKTHROUGH_AREA[0].RESULT+'\\n \\
					Function : '+result.DATA_MASTER_WALKTHROUGH_AREA[0].MESSAGE+'\\n \\
					', "success");

				initAreaMaster();
			} else {
				\$.notify('GAGAL !\\n\\nGagal menghapus data master area :\\n \\
					Status : '+result.DATA_MASTER_WALKTHROUGH_AREA[0].RESULT+'\\n \\
					Function : '+result.DATA_MASTER_WALKTHROUGH_AREA[0].MESSAGE+'\\n \\
					', "error");

				initAreaMaster();
			}
		}
		
		function onResetAddFields(){
			\$('#addAreaBU').val("");
			\$('#addAreaDiv').val("");
			\$('#addAreaLokasi').val("");
			\$('#addAreaWilayah').val("");
			\$('#addIsfstand').val("");
		}
		
		function onError(e){
			console.log(e);
		}
	</script>
  </body>
</html>
~;
}