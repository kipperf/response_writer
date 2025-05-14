import streamlit as st

def get_formatted_response():
    """
    Get a formatted response based on content from all tabs.
    Returns a markdown formatted string.
    """
    response = ''

    ###########
    # Notes ##
    ###########

    response += '# **_Notes_**\n\n' 

    notes_input = st.session_state.get('notes_content', '')
    response += notes_input
    response += '\n\n'



    ###########
    # Overview #
    ###########
    response += '# **_Overview_**\n\n'
    
    # Get the content from the FRA and relevant documents section
    fra_submitted = st.session_state.get('fra_submitted', False)
    fra_details = st.session_state.get('fra_details', '')
    relevant_documents_submitted = st.session_state.get('relevant_documents_submitted', False)
    relevant_documents = st.session_state.get('relevant_documents', '')

    fra_section_text = generate_fra_section_text(
        fra_submitted, 
        fra_details, 
        relevant_documents_submitted, 
        relevant_documents
    )

    response += fra_section_text


    # Get the content from the Development Details section
    application_type = st.session_state.get('application_type', '')
    existing_vulnerability_classification = st.session_state.get('existing_vulnerability_classification', '')
    proposed_vulnerability_classification = st.session_state.get('proposed_vulnerability_classification', '')

    development_details_section_text = generate_development_details_section_text(
        application_type,
        existing_vulnerability_classification,
        proposed_vulnerability_classification
    )

    response += development_details_section_text


    # Get the content from the Flood Zone and Modelling section
    flood_zone_defined = st.session_state.get('flood_zone_defined', False)
    flood_zone = st.session_state.get('flood_zone', '')
    flood_model = st.session_state.get('flood_model', '')
    model_status = st.session_state.get('model_status', '')
    model_name = st.session_state.get('model_name', '')
    model_year = st.session_state.get('model_year', '')


    flood_zone_section_text = generate_flood_zone_section_text(
        flood_zone_defined,
        flood_zone,
        flood_model,
        model_status,
        model_name,
        model_year,
    )

    response += flood_zone_section_text


    # get the content from the climate change section
    climate_change_relevant = st.session_state.get('climate_change_relevant', False)
    climate_change_reason = st.session_state.get('climate_change_reason', '')
    climate_change_allowance = st.session_state.get('climate_change_allowance', '')
    correct_climate_change_allowance = st.session_state.get('correct_climate_change_allowance', False)
    correct_climate_change_allowance_value = st.session_state.get('correct_climate_change_allowance_value', '')


    climate_change_section_text = generate_climate_change_section_text(
        climate_change_relevant,
        climate_change_reason,
        climate_change_allowance,
        correct_climate_change_allowance,
        correct_climate_change_allowance_value
    )

    response += climate_change_section_text


    # get the content from the finished floor levels section
    finished_floor_levels_relevant = st.session_state.get('finished_floor_levels_relevant', False)
    finished_floor_levels = st.session_state.get('finished_floor_levels', '')
    finished_floor_levels_acceptable = st.session_state.get('finished_floor_levels_acceptable', False)
    finished_floor_levels_reason = st.session_state.get('finished_floor_levels_reason', '')
    finished_floor_levels_reason_other = st.session_state.get('finished_floor_levels_reason_other', '')

    finished_floor_levels_section_text = generate_finished_floor_levels_section_text(
        finished_floor_levels_relevant,
        finished_floor_levels,
        finished_floor_levels_acceptable,
        finished_floor_levels_reason,
        finished_floor_levels_reason_other
    )

    response += finished_floor_levels_section_text
    


    # get the content from the flood defences section
    flood_defences = st.session_state.get('flood_defences', False)
    flood_defences_count = st.session_state.get('flood_defences_count', '')
    breach_and_over_topping_analysis = st.session_state.get('breach_and_over_topping_analysis', False)
    breach_and_over_topping_analysis_done = st.session_state.get('breach_and_over_topping_analysis_done', False)
    acceptable_breach_and_over_topping_analysis = st.session_state.get('acceptable_breach_and_over_topping_analysis', False)
    breach_and_over_topping_analysis_result = st.session_state.get('breach_and_over_topping_analysis_result', '')
    breach_and_over_topping_analysis_reason = st.session_state.get('breach_and_over_topping_analysis_reason', '')

    flood_defences_section_text = generate_flood_defences_section_text(
        flood_defences,
        flood_defences_count,
        breach_and_over_topping_analysis,
        breach_and_over_topping_analysis_done,
        acceptable_breach_and_over_topping_analysis,
        breach_and_over_topping_analysis_result,
        breach_and_over_topping_analysis_reason
    )

    response += flood_defences_section_text



    # get third party flood risk assessment section
    development_displaces_flood_water = st.session_state.get('development_displaces_flood_water', '')
    mitigation_put_in_place = st.session_state.get('mitigation_put_in_place', False)
    mitigation_type = st.session_state.get('mitigation_type', '')
    flood_plain_compensation_type = st.session_state.get('flood_plain_compensation_type', '')
    mitigation_acceptable = st.session_state.get('mitigation_acceptable', False)
    mitigation_acceptable_reason = st.session_state.get('mitigation_acceptable_reason', '')
    mitigation_other_type = st.session_state.get('mitigation_other_type', '')

    third_party_flood_risk_assessment_section_text = generate_third_party_flood_risk_assessment_section_text(
        development_displaces_flood_water,
        mitigation_put_in_place,
        mitigation_type,
        flood_plain_compensation_type,
        mitigation_acceptable,
        mitigation_acceptable_reason,
        mitigation_other_type
    )   

    response += third_party_flood_risk_assessment_section_text
    

    # get the content from the design flood level section
    design_flood_level_calculated = st.session_state.get('design_flood_level_calculated', False)
    design_flood_level = st.session_state.get('design_flood_level', '')
    design_flood_level_acceptable = st.session_state.get('design_flood_level_acceptable', False)
    design_flood_level_reason = st.session_state.get('design_flood_level_reason', '')
    design_flood_level_reason_other = st.session_state.get('design_flood_level_reason_other', '')

    design_flood_level_section_text = generate_design_flood_level_section_text(
        design_flood_level_calculated,
        design_flood_level,
        design_flood_level_acceptable,
        design_flood_level_reason,
        design_flood_level_reason_other
    )

    response += design_flood_level_section_text


    # get the content from the access and egress section
    access_and_egress_considered = st.session_state.get('access_and_egress_considered', False)
    access_and_egress_position = st.session_state.get('access_and_egress_position', '')
    access_and_egress_position_agreed = st.session_state.get('access_and_egress_position_agreed', '')
    access_and_egress_position_reason = st.session_state.get('access_and_egress_position_reason', '')
    access_and_egress_data = st.session_state.get('access_and_egress_data', False)
    access_and_egress_data_text = st.session_state.get('access_and_egress_data_text', '')
    access_and_egress_acceptable = st.session_state.get('access_and_egress_acceptable', '')
    access_and_egress_reason = st.session_state.get('access_and_egress_reason', '')
    
    access_and_egress_section_text = generate_access_and_egress_section_text(
        access_and_egress_considered,
        access_and_egress_position,
        access_and_egress_position_agreed,
        access_and_egress_position_reason,
        access_and_egress_data,
        access_and_egress_data_text,
        access_and_egress_acceptable,
        access_and_egress_reason
    )
    
    response += access_and_egress_section_text
    
    # get the content from the easement section
    easement_issue = st.session_state.get('easement_issue', '')
    easement_issue_reason = st.session_state.get('easement_issue_reason', '')
    easement_resolution = st.session_state.get('easement_resolution', '')
    
    easement_section_text = generate_easement_section_text(
        easement_issue,
        easement_issue_reason,
        easement_resolution
    )
    
    response += easement_section_text

    # get the content from the required contributions section
    required_contributions = st.session_state.get('required_contributions', '')
    required_contributions_type = st.session_state.get('required_contributions_type', [])
    required_contributions_other = st.session_state.get('required_contributions_other', '')
    total_contributions_required = st.session_state.get('total_contributions_required', 0)
    required_contributions_reason = st.session_state.get('required_contributions_reason', '')
    
    required_contributions_section_text = generate_required_contributions_section_text(
        required_contributions,
        required_contributions_type,
        required_contributions_other,
        total_contributions_required,
        required_contributions_reason
    )
    
    response += required_contributions_section_text

    # get the content from the flood resilient and resistant construction section
    flood_resilient_and_resistant_construction = st.session_state.get('flood_resilient_and_resistant_construction', '')
    flood_resilient_and_resistant_construction_acceptable = st.session_state.get('flood_resilient_and_resistant_construction_acceptable', False)
    flood_resilient_and_resistant_construction_reason = st.session_state.get('flood_resilient_and_resistant_construction_reason', '')
    
    flood_resilient_resistant_construction_section_text = generate_flood_resilient_resistant_construction_section_text(
        flood_resilient_and_resistant_construction,
        flood_resilient_and_resistant_construction_acceptable,
        flood_resilient_and_resistant_construction_reason
    )
    
    response += flood_resilient_resistant_construction_section_text
    
    # get the additional information
    overview_input = st.session_state.get('overview_input', '')
    
    additional_information_text = generate_additional_information_section_text(overview_input)
    
    response += additional_information_text




    # National Standard Paragraph
    national_standard_paragraph_text = generate_national_standard_paragraph()

    response += national_standard_paragraph_text







    return response

def update_response():
    """Callback function for form changes (for compatibility)"""
    # This is left empty as rerendering happens automatically
    pass



def generate_national_standard_paragraph():
    """
    Generate the national standard paragraph based on the form data.
    """

    nsp_text = '\n\n# **__Environment Agency position__**\n'

    response_points_dict = check_selected_nsp_response_points_checkboxes()

    overarching_response_type = st.session_state.get('nsp_overarching_response_type', '')

    if overarching_response_type == "No Objection - Condition":
        nsp_text += '**No Objection - Condition**\n'
        sub_type = st.session_state.get('nsp_sub_type_no_objection_condition', '')
        nsp_text += f'{sub_type}\n'

    elif overarching_response_type == "No Objection - No Condition":
        nsp_text += '**No Objection - No Condition**\n'
        sub_type = st.session_state.get('nsp_sub_type_no_objection_no_condition', '')
        nsp_text += f'{sub_type}\n'

    elif overarching_response_type == "Objection - In Detail":
        sub_type = st.session_state.get('nsp_sub_type_objection_in_detail', '')
       
        if sub_type == "Inadequate FRA Submitted":
            nsp_text +=  "**Environment Agency position**\n\n"
            nsp_text +=  "In the absence of an acceptable Flood Risk Assessment (FRA) we object to this application and recommend that planning permission is refused. \n\n"
            nsp_text +=  "**Reason(s)**\n\n"
            nsp_text +=  "The submitted FRA does not comply with the requirements for site-specific flood risk assessments, as set out in paragraphs 30 to 32 of the Flood Risk and Coastal Change section of the planning practice guidance. The FRA does not therefore adequately assess the development's flood risks. In particular, the FRA fails to:\n\n"
            
            for key, value in response_points_dict.items():
                if value:
                    nsp_text += sub_response_points_text(key)

    elif overarching_response_type == "Objection - In Principle":
        nsp_text += '**Objection - In Principle**\n'
        sub_type = st.session_state.get('nsp_sub_type_objection_in_principle', '')
        nsp_text += f'{sub_type}\n'
    



    return nsp_text



def sub_response_points_text(key):
    """
    Returns the appropriate text response based on the checkbox key.
    
    Args:
        key: The key of the checkbox from session state
        
    Returns:
        str: The text to include in the response for this specific issue
    """
    
    if key == 'nsp_condition_inadequate_fra_submitted_flood_zone_not_defined':
        return "- Set out the flood zone that the proposal lies within.\n"
    
    elif key == 'nsp_condition_inadequate_fra_submitted_development_incompatible_with_the_flood_zone':
        flood_zone = st.session_state.get('flood_zone', '')
        proposed_vulnerability_classification = st.session_state.get('proposed_vulnerability_classification', '')
        
        if len(flood_zone) == 0:
            return "- SET YOUR FLOOD ZONE. \n"
        elif len(flood_zone) == 1:
            flood_zone_text = flood_zone[0]
        elif len(flood_zone) == 2:
            flood_zone_text = f"{flood_zone[0]} and {flood_zone[1]}"
        else:
            flood_zone_text = f"{', '.join(flood_zone[:-1])}, and {flood_zone[-1]}"
            
        sub_response_text = f"- Set devlopment in a flood zone compatible with the vulnerability classification. "
        sub_response_text += f"The development is in the flood zone{'' if len(flood_zone) == 1 else 's'} {flood_zone_text} and the vulnerability classification is {proposed_vulnerability_classification}.\n"
        return sub_response_text
    
    elif key == 'nsp_condition_inadequate_fra_submitted_acceptable_model_not_used':
        model_status = st.session_state.get('model_status', '')
        return f"- Use an acceptable model to assess flood risk. The models review status is: {model_status}.\n"
    
    elif key == 'nsp_condition_inadequate_fra_submitted_incorrect_climate_change_allowance_used':
        climate_change_allowance = st.session_state.get('climate_change_allowance', '')
        correct_climate_change_allowance_value = st.session_state.get('correct_climate_change_allowance_value', '')

        if climate_change_allowance == 0:
            sub_response_text = f"- Use the correct climate change allowance. The submission has not applied any climate change allowance. "
        else:
            sub_response_text = f"- Use the correct climate change allowance. The submission has applied a climate change allowance of {climate_change_allowance}%. "
        
        sub_response_text += f"The correct climate change allowance is {correct_climate_change_allowance_value}%.\n"

        return sub_response_text
        

    elif key == 'nsp_condition_inadequate_fra_submitted_incorrect_design_flood_level_used_wrong_node_point':
        return "- Use the correct node point to determine the design flood level. The cloest upstream node point is used to determine the design flood level.\n"
    
    elif key == 'nsp_condition_inadequate_fra_submitted_incorrect_design_flood_level_used_inappropriate_interpolation':
        return "- Use appropriate methods to determine the design flood level. Interpolation is not appropriate for this devlopment.\n"
    
    elif key == 'nsp_condition_inadequate_fra_submitted_finished_floor_levels_not_high_enough':
        how_much_freeboard = st.session_state.get('how_much_freeboard', 0)
        return f"- Ensure finished floor levels are set sufficiently above the design flood level. The requiredfreeboard is {how_much_freeboard}mm above the design flood level.\n"
    
    elif key == 'nsp_condition_inadequate_fra_submitted_residual_risk_behind_defences_not_assessed':
        return "- Assess the residual risk behind defences. This includes both breach and overtopping assessments\n"
    
    elif key == 'nsp_condition_inadequate_fra_submitted_residual_risk_behind_defences_not_adequately_assessed':
        return "- Adequately assess the residual risk behind defences for both breach and overtopping.\n"
    
    elif key == 'nsp_condition_inadequate_fra_submitted_third_party_impacts_not_assessed':
        return "- Properly assess the impacts on third parties. There should be no loss of floodplain storage capacity on a level-for-level and volume-for-volume basis.\n"
    
    elif key == 'nsp_condition_inadequate_fra_submitted_floodplain_compensation_not_level_for_level_and_volume_for_volume':
        return "- Provide floodplain compensation on a level-for-level and volume-for-volume basis. The cumulative storage volume provided is avabile at or before the slice it is needed when assessing in 200mm slices from the lowest level on the site\n"
    
    elif key == 'nsp_condition_inadequate_fra_submitted_floodplain_compensation_not_volume_for_volume':
        return "- Provide floodplain compensation on a volume-for-volume basis. The cumulative storage volume provided is avabile at or before the slice it is needed when assessing in 200mm slices from the lowest level on the site\n"
    
    elif key == 'nsp_condition_inadequate_fra_submitted_third_party_food_risk_mitigation_measures_not_adequate':
        return "- Provide adequate flood risk mitigation measures for third parties. The measures should demonstrate no detrimental impact to others\n"
    
    elif key == 'nsp_condition_inadequate_fra_submitted_access_and_egress_routes_not_properly_assessed':
        return "- Properly assess access and egress routes. Access and egress should be through the lowest risk parts of the site wherever possible\n"
    
    elif key == 'nsp_condition_inadequate_fra_submitted_inadequate_easement_from_a_watercourse':
        easement_issue_reason = st.session_state.get('easement_issue_reason', '')
        easement_resolution = st.session_state.get('easement_resolution', '')
        return f"- Provide adequate easement from the watercourse. {easement_issue_reason}. To resolve this issue, {easement_resolution}\n"
    
    elif key == 'nsp_condition_inadequate_fra_submitted_inadequate_easement_from_a_flood_defence':
        easement_issue_reason = st.session_state.get('easement_issue_reason', '')
        easement_resolution = st.session_state.get('easement_resolution', '')
        return f"- Provide adequate easement from the flood defence. {easement_issue_reason}. To resolve this issue, {easement_resolution}\n"
    
    
    elif key == 'nsp_condition_inadequate_fra_submitted_contributions_not_agreed':

        total_contributions_required = st.session_state.get('total_contributions_required', '')
        required_contributions_type = st.session_state.get('required_contributions_type', [])
        required_contributions_reason = st.session_state.get('required_contributions_reason', '')
        required_contributions_other = st.session_state.get('required_contributions_other', '')

        contrbuton_text = f"- Agree to the required contributions. The required contributions are £{total_contributions_required}. "
        contrbuton_text += f"These are required for:\n"

        for i in range(len(required_contributions_type)):
            contrbuton_text += f"   - {required_contributions_type[i]}\n"
        
        if required_contributions_other:
            contrbuton_text += f"   - {required_contributions_other}\n"
        
        contrbuton_text += f"\n The reason for the required contributions is: {required_contributions_reason}\n"
        return contrbuton_text


    elif key == 'nsp_condition_inadequate_fra_submitted_flood_resilient_and_resistant_construction_not_used':
        return "- Propose suitable flood resilient and resistant construction methods.\n"
    
    elif key == 'nsp_condition_inadequate_fra_submitted_flood_resilient_and_resistant_construction_not_adequate':
        return "- Propose suitable flood resilient and resistant construction methods.\n"
    
    # No Objection - No Condition responses
    elif key == 'nsp_no_objection_no_condition_no_flood_risk':
        return "- The site is at no risk of flooding.\n"
    
    elif key == 'nsp_no_objection_no_condition_very_low_flood_risk':
        return "The site is at very low risk of flooding.\n"
    else:
        return ""



def check_selected_nsp_response_points_checkboxes():
    """
    Returns a dictionary of checkbox keys and their values for the National Standard Paragraphs section.
    Includes NSP-related checkbox keys with the specified prefixes.
    """
    # List of acceptable key prefixes - keep this list up to date when adding new checkbox types
    acceptable_prefixes = [
        'nsp_condition_',
        'nsp_no_objection'
    ]
    
    response_points_dict = {}
    
    # Iterate through all session state keys
    for key in st.session_state:
        # Check if key starts with any of the acceptable prefixes
        if any(key.startswith(prefix) for prefix in acceptable_prefixes):
            response_points_dict[key] = st.session_state.get(key, False)
    
    return response_points_dict




def generate_fra_section_text(
        fra_submitted, 
        fra_details, 
        relevant_documents_submitted, 
        relevant_documents
    ):

    text = '**Flood Risk Assessment (FRA) Details**\n\n'
    
    if fra_submitted:
        text += f'An FRA has been submitted and reviewed in support of this application ({fra_details}). '
    else:
        text += f'An FRA has not been submitted in support of this application. '

    if relevant_documents_submitted:
        text += f'Other relevant documents which support an FRA have been submitted and reviewed ({relevant_documents}). '
    else:
        text += f'Other relevant documents which support an FRA have not been submitted. '
    
    text += 'We reviewed all submitted plans.'
    

    return text


def generate_development_details_section_text(
        application_type,
        existing_vulnerability_classification,
        proposed_vulnerability_classification
    ):

    text = '\n\n**Development Details**\n\n'

    if application_type == 'Outline':
        text += f'The application is an {application_type} application. '
    else:
        text += f'The application is a {application_type} application. '


    if application_type == 'Change of Use':
        text += f'The existing vulnerability classification is {existing_vulnerability_classification}. '

    text += f'The proposed vulnerability classification is {proposed_vulnerability_classification}. '

    return text
    

def generate_flood_zone_section_text(
        flood_zone_defined,
        flood_zone,
        flood_model,
        model_status,
        model_name,
        model_year,
    ):

    text = '\n\n**Flood Zone and Modelling Details**\n\n'

    if not flood_zone_defined:
        text += f'The submission does not demonstrate which flood zones the site sits within. '
    else:
        if len(flood_zone) == 1:
            text += f'The submission states that the site sits within {flood_zone[0]}. '
        elif len(flood_zone) == 0:
            text += f'PLEASE ENTER THE FLOOD ZONE. '
        else:
            text += f'The submission states that the site sits within {", ".join(flood_zone[:-1])} and {flood_zone[-1]}. '

    if flood_model == 'EA Model':
        text += f'The flood model used is an Environment Agency (EA) model. '
        if model_name and model_year:
            text += f'The model used is the {model_name} ({model_year}). '
    elif flood_model == 'New National Modelling':
        text += f'The flood model used is the New National Modelling (NNM) model. '
    elif flood_model == 'Applicant Model':
        text += f'The flood model used is the applicant\'s model. '

    if flood_model != 'New National Modelling':
        if model_status == 'Not Reviewed (review not needed)':
            text += f'The model has not been reviewed. It is the applicants job to provide a suitable flood model has so no review of this model has been undertaken to verify this. '
        elif model_status == 'Not Reviewed (review needed)':
            text += f'The model has not been reviewed. The model must first undergo a review to determine if it is an acceptable representation of flood risk to the site. '
        elif model_status == 'Reviewed and approved':
            text += f'The model has been reviewed and approved. '
        elif model_status == 'Reviewed and rejected':
            text += f'The model has been reviewed and rejected, details of the review are attached to this response. '
        elif model_status == 'Approved EA Model':
            text += f'The model uses an approved EA model which is suitable to be used for this site. '
        elif model_status == 'EA Model not suitable to be used for this site':
            text += f'The model uses an EA model which is not suitable to be used for this site. '


    return text


def generate_climate_change_section_text(
        climate_change_relevant,
        climate_change_reason,
        climate_change_allowance,
        correct_climate_change_allowance,
        correct_climate_change_allowance_value
    ):

    text = '\n\n**Climate Change Details**\n\n'

    if climate_change_relevant:
        text += f'The climate change allowance used in the FRA is {climate_change_allowance}%. '
        if correct_climate_change_allowance:
            text += f'This is the correct climate change allowance. '
        else:
            text += f'This is not the correct climate change allowance. The correct climate change allowance is {correct_climate_change_allowance_value}%. '

    
    if not climate_change_relevant:
        text += f'Climate change allowance is not relevant to this application as {climate_change_reason}. '

    
    return text


def generate_finished_floor_levels_section_text(
        finished_floor_levels_relevant,
        finished_floor_levels,
        finished_floor_levels_acceptable,
        finished_floor_levels_reason,
        finished_floor_levels_reason_other
    ):

    text = '\n\n**Finished Floor Levels Details**\n\n'

    if finished_floor_levels_relevant:
        text += f'Finished floor levels are relevant to this application. '

        if finished_floor_levels:
            text += f'The finished floor levels are {finished_floor_levels}. '

            if finished_floor_levels_acceptable:
                text += f'The finished floor levels are acceptable. '
            else:
                if finished_floor_levels_reason == 'Other':
                    text += f'The finished floor levels are not acceptable due to {finished_floor_levels_reason_other}. '
                else:
                    text += f'The finished floor levels are not acceptable due to {finished_floor_levels_reason}. '



        else:
            text += f'The finished floor levels are not provided. '






    else:
        text += f'The finished floor levels are not relevant to this application. '

    return text


def generate_flood_defences_section_text(
        flood_defences,
        flood_defences_count,
        breach_and_over_topping_analysis,
        breach_and_over_topping_analysis_done,
        acceptable_breach_and_over_topping_analysis,
        breach_and_over_topping_analysis_result,
        breach_and_over_topping_analysis_reason
    ):


    text = '\n\n**Flood Defences Details**\n\n'

    if not flood_defences:
        text += f'There are no flood defences relevant to this application. '
        return text
    else:
        text += f'There are {flood_defences_count} flood defence(s) relevant to this application. '

        for i in range(flood_defences_count):
            defence_name = st.session_state.get(f'defence_name_{i}', '')
            defence_sop = st.session_state.get(f'defence_sop_{i}', '')
            text += f'Flood defence {i+1} is {defence_name} with a Standard of Protection (SOP) of {defence_sop}. '
        

        if breach_and_over_topping_analysis:
            text += f'A breach and overtopping analysis is required for this application. '
            if breach_and_over_topping_analysis_done:
                text += f'A breach and overtopping analysis has been undertaken. '
                if acceptable_breach_and_over_topping_analysis:
                    text += f'The breach and overtopping analysis is acceptable. '

                    if breach_and_over_topping_analysis_result:
                        text += f'The breach and overtopping analysis shows that the site is at risk. '
                    else:
                        text += f'The breach and overtopping analysis shows that the site is not at risk. '                    
                else:
                    text += f'The breach and overtopping analysis is not acceptable due to {breach_and_over_topping_analysis_reason} '
            else:
                text += f'A breach and overtopping analysis has not been undertaken. '
        else:
            text += f'A breach and overtopping analysis is not required for this application. '




        




    return text


def generate_third_party_flood_risk_assessment_section_text(
        development_displaces_flood_water,
        mitigation_put_in_place,
        mitigation_type,
        flood_plain_compensation_type,
        mitigation_acceptable,
        mitigation_acceptable_reason,
        mitigation_other_type
    ):

    text = '\n\n**Third Party Flood Risk Assessment Details**\n\n'

    if development_displaces_flood_water:
        text += f'The development displaces flood water in the design flood event. '

        if mitigation_put_in_place:
            text += f'Mitigation has been put in place to protect the third parties from increased flood risk. '

            if mitigation_type == 'Flood plain compensation':
                text += f'The mitigation proposed is flood plain compensation '

                if flood_plain_compensation_type == "Level-for-Level and Volume-for-Volume":
                    text += f'which is on a Level-for-Level and Volume-for-Volume basis. '
                elif flood_plain_compensation_type == "Volume-for-Volume":
                    text += f'which is on a Volume-for-Volume basis. '
                else:
                    text += f'which is not on a Level-for-Level or Volume-for-Volume basis. '

                if mitigation_other_type:
                    text += f'The proposed mitigation is {mitigation_other_type}. '

            if mitigation_acceptable:
                text += f'The mitigation proposed is acceptable. '
            else:
                text += f'The mitigation proposed is not acceptable due to {mitigation_acceptable_reason}. '
 
                
        else:
            text += f'No mitigation has been put in place to protect the third parties from increased flood risk from the reduced floodplain storage capacity. '


    else:
        text += f'The development does not displace flood water in the design flood event. On that basis there will be no third party impacts'


    return text


def generate_design_flood_level_section_text(
        design_flood_level_calculated,
        design_flood_level,
        design_flood_level_acceptable,
        design_flood_level_reason,
        design_flood_level_reason_other
    ):

    text = '\n\n**Design Flood Level Details**\n\n'

    if design_flood_level_calculated:
        text += f'The FRA states that the design flood level is {design_flood_level}. '

        if design_flood_level_acceptable:
            text += f'This is an acceptable design flood level. '
        else:
            if design_flood_level_reason == 'Other':
                text += f'This is not an acceptable design flood level as {design_flood_level_reason_other}. '
            else:
                text += f'This is not an acceptable design flood level as {design_flood_level_reason}. '
    else:
        text += f'The FRA does not include a design flood level. '

    return text


def generate_access_and_egress_section_text(
        access_and_egress_considered,
        access_and_egress_position,
        access_and_egress_position_agreed,
        access_and_egress_position_reason,
        access_and_egress_data,
        access_and_egress_data_text,
        access_and_egress_acceptable,
        access_and_egress_reason
    ):
    
    text = '\n\n**Access and Egress Details**\n\n'
    
    if access_and_egress_considered:
        text += f'Access and egress has been considered as part of this application. '
        
        # Handle the case where position is "Other"
        if access_and_egress_position == "Other":
            access_and_egress_position_other = st.session_state.get('access_and_egress_position_other', '')
            text += f'The FRA states that the access and egress position is "{access_and_egress_position_other}". '
        else:
            text += f'The FRA states that the access and egress position is "{access_and_egress_position}". '
        
        # Handle Yes/No/Not enough information provided radio options
        if access_and_egress_position_agreed == "Yes":
            text += f'We agree with this position. '
        elif access_and_egress_position_agreed == "No":
            text += f'We do not agree with this position. '
        elif access_and_egress_position_agreed == "Not enough information provided":
            text += f'We cannot confirm if we agree with this position as not enough information has been provided. '
            
        if access_and_egress_position_reason:
            text += f'{access_and_egress_position_reason} '
            
        if access_and_egress_data:
            text += f'Our data shows that {access_and_egress_data_text}. '
    else:
        text += f'Access and egress has not been considered as part of this application. '
    
    if access_and_egress_acceptable == 'Acceptable':
        text += f'The consideration of access and egress is acceptable. '
    elif access_and_egress_acceptable == 'Not acceptable':
        text += f'The consideration of access and egress is not acceptable. '
    elif access_and_egress_acceptable == 'For LPA to determine':
        text += f'The consideration of access and egress is for the Local Planning Authority to determine. '
    
    if access_and_egress_reason:
        text += f'Our position is on the basis that {access_and_egress_reason}. '
    
    text += '\nPlease note that we are not staturtory consultees on access and egress, the LPA should consult with its emergency planners.'
    
    return text


def generate_easement_section_text(
        easement_issue,
        easement_issue_reason,
        easement_resolution
    ):
    
    text = '\n\n**Easement Details**\n\n'
    
    if easement_issue == "Yes":
        text += f'There is an issue with the easement for this site. '
        
        if easement_issue_reason:
            text += f'{easement_issue_reason} '
            
        if easement_resolution:
            text += f'To resolve this issue: {easement_resolution}'
            
    elif easement_issue == "No":
        text += f'There are no issues with the easement for this site. '
        
        if easement_issue_reason:
            text += f'{easement_issue_reason}'
            
    elif easement_issue == "Unclear":
        text += f'It is unclear whether there are issues with the easement for this site. '
        
        if easement_issue_reason:
            text += f'{easement_issue_reason} '
            
        if easement_resolution:
            text += f'Our recommendation is: {easement_resolution}'
    
    return text


def generate_required_contributions_section_text(
        required_contributions,
        required_contributions_type,
        required_contributions_other,
        total_contributions_required,
        required_contributions_reason
    ):
    
    text = '\n\n**Required Contributions**\n\n'
    
    if required_contributions == "Yes":
        text += f'Financial contributions will be required as part of this development. '
        
        if required_contributions_type:
            if len(required_contributions_type) == 1:
                text += f'The contribution is for {required_contributions_type[0].lower()}. '
            else:
                formatted_types = [item.lower() for item in required_contributions_type]
                last_type = formatted_types.pop()
                text += f'The contributions are for {", ".join(formatted_types)} and {last_type}. '
            
            if "Other" in required_contributions_type and required_contributions_other:
                text += f'The other contribution is for {required_contributions_other}. '
        
        if total_contributions_required:
            text += f'The total contribution required is £{total_contributions_required:,}. '
        
        if required_contributions_reason:
            text += f'These contributions are required because {required_contributions_reason}'
            
    else:
        text += f'No financial contributions will be required as part of this development.'
    
    return text


def generate_flood_resilient_resistant_construction_section_text(
        flood_resilient_and_resistant_construction,
        flood_resilient_and_resistant_construction_acceptable,
        flood_resilient_and_resistant_construction_reason
    ):
    
    text = '\n\n**Flood Resilient and Resistant Construction**\n\n'
    
    if flood_resilient_and_resistant_construction == "Yes":
        text += f'The development includes flood resilient and resistant construction measures. '
        
        if flood_resilient_and_resistant_construction_acceptable:
            text += f'These measures are acceptable. '
        else:
            text += f'These measures are not acceptable. '
            
            if flood_resilient_and_resistant_construction_reason:
                text += f'The reason for this is: {flood_resilient_and_resistant_construction_reason}'
                
    elif flood_resilient_and_resistant_construction == "No":
        text += f'The development does not include flood resilient and resistant construction measures. '
        
        if flood_resilient_and_resistant_construction_acceptable:
            text += f'This is considered acceptable. '
            
            if flood_resilient_and_resistant_construction_reason:
                text += f'The reason for this is: {flood_resilient_and_resistant_construction_reason}'
        else:
            text += f'This is not considered acceptable. Flood resilient and resistant construction measures should be incorporated into the design.'
    
    return text


def generate_additional_information_section_text(overview_input):
    
    text = ''
    
    if overview_input and overview_input.strip():
        text = '\n\n**Additional Information**\n\n'
        text += overview_input
    
    return text



