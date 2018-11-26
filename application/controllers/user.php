<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class user extends CI_Controller {
	
	function __construct()
	{
	   parent::__construct();
	}
 
	// user data mapping links

	public function user_profile()
	{
		$this->load->view('welcome_message');
	}
	
	public function user_data()
	{
		$this->load->view('welcome_message');
	}
	
}
