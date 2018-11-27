<?php

class campaign_model extends CI_Model{

    /**
    *   retrieve all campaign
    */
    public function retrieveAllCampaign(){
		$result = array();
		
			$this->db->select('*');
			$this->db->from('srn_campaign');
			$query = $this->db->get();
			$resultQuery = $query->result();
			$result[] = array("data" => $resultQuery);

		return json_encode($result);
    }
	
	/**
    *   retrieve one campaign
    */
	public function retrieveOneCampaign($data){
		$result = array();
		
			$this->db->select('*');
			$this->db->from('srn_campaign');
			$this->db->where('id', $id);
			$query = $this->db->get();
			$resultQuery = $query->result();
			$result[] = array("data" => $resultQuery);

		return json_encode($result);
	}
	
	/**
    *   save a new campaign
    */
	public function saveNewCampaign($data){
		$result = array();
		
			$insertData = array(
				'brand_id' => $brand_id,
				'campaign_type' => $campaign_type,
				'campaign_name' => $campaign_name,
				'description' => $description,
				'tnc' => $tnc,
				'start_date' => $start_date,
				'end_date' => $end_date,
				'is_active' => $is_active,
				'required_points' => $required_points,
				'created' => $created,
				'last_updated' => $last_updated
			);
			
			$sth = $this->db->insert('srn_campaign', $insertData);
			
			//$sth = $db->prepare("INSERT INTO srn_campaign (brand_id, campaign_type, campaign_name, description, tnc, start_date, end_date, is_active, required_points, created, last_updated) VALUES (?,?,?,?,?,?,?,?,?,?,?)");
			//$sth->execute(array($brand_id, $campaign_type, $campaign_name, $description, $tnc, $start_date, $end_date, $is_active, $required_points, $created, $last_updated));
			$affected_rows = $sth->rowCount();
			$resultNotes = ($affected_rows == 1) ? "SUCCESS" : "FAILURE";
			$result[] = array("result" => $resultNotes, "affected_rows" => $affected_rows);
		
		return json_encode($result);
	}
	
	/**
    *   edit campaign data
    */
	public function editCampaign($data){
		$result = array();
		
			$updateData = array(
					'brand_id' => $brand_id,
					'campaign_type' => $campaign_type,
					'campaign_name' => $campaign_name,
					'description' => $description,
					'tnc' => $tnc,
					'start_date' => $start_date,
					'end_date' => $end_date,
					'is_active' => $is_active,
					'required_points' => $required_points,
					'created' => $created,
					'last_updated' => $last_updated
				);
			$this->db->where('id', $id);
			$sth = $this->db->update('srn_campaign', $updateData);
		
			$affected_rows = $sth->rowCount();
			$resultNotes = ($affected_rows == 1) ? "SUCCESS" : "FAILURE";
			$result[] = array("result" => $resultNotes, "affected_rows" => $affected_rows);
		
		return json_encode($result);
	}
	
	/**
    *   delete campaign data
    */
	public function deleteCampaign($data){
		$result = array();
		
			$sth = $this->db->delete('srn_campaign', array('id' => $id));
		
			$affected_rows = $sth->rowCount();
			$resultNotes = ($affected_rows == 1) ? "SUCCESS" : "FAILURE";
			$result[] = array("result" => $resultNotes, "affected_rows" => $affected_rows);
		
		return json_encode($result);
	}
	
	/*** EOF campaign_model.php */
}

?>