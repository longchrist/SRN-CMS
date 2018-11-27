<?php

class brand_model extends CI_Model{

    /**
    *   retrieve all brand
    */
    public function retrieveAllBrands(){
		$result = array();
		//$result = "";
			$this->db->select('*');
			$this->db->from('srn_brand');
			$query = $this->db->get();
			$resultQuery = $query->result();
			//$projects_count = count($query->result());
			$result[] = array("data" => $resultQuery);

		return json_encode($result);
    }
	
	/**
    *   retrieve one brand
    */
	public function retrieveOneBrand(){
		
	}
	
	/**
    *   save a new brand
    */
	public function saveNewBrand(){
		
	}
	
	/**
    *   edit brand data
    */
	public function editBrand(){
		
	}
	
	/**
    *   delete brand data
    */
	public function deleteBrand(){
		
	}
	
	/*** EOF brand_model.php */
}

?>