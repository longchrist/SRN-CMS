<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class brand extends CI_Controller {
	
	function __construct()
	{
	   parent::__construct();
	   $this->load->model('brand_model');
	}
 
	// user data mapping links

	public function getAllBrand()
	{
		return $this->output
            ->set_content_type('application/json')
            ->set_status_header(200)
            ->set_output($this->brand_model->retrieveAllBrands());
            
	}
	
	public function master_brand()
	{
		$this->load->view('master_brand');
	}
	
}

?>
