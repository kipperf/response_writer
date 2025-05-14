import streamlit as st
from generate_response.generate_response import update_response




def render_national_standard_paragraphs():
    """Render the content for the National Standard Paragraphs tab"""
    st.header("National Standard Paragraphs")
    

    # Select the overarching response type
    response_type = st.selectbox(
        label="Select the overarching response type",
        options=["No Objection - Condition", "No Objection - No Condition", "Objection - In Detail", "Objection - In Principle"],
        key="nsp_overarching_response_type",
        on_change=update_response
    )

    # Render the response type specific content
    if response_type == "No Objection - Condition":
        no_objection_condition()
    elif response_type == "No Objection - No Condition":
        no_objection_no_condition()
    elif response_type == "Objection - In Detail":
        objection_in_detail()
    elif response_type == "Objection - In Principle":
        objection_in_principle()


def no_objection_condition():

    options = [
        "Secure Implementation of the FRA",
        "Scheme to be agreed - Issue not addressed / addressed satisfactorily in the FRA",
        "Outline Application - Scheme to be agreed at reserved matters",
        "Details of an appropriate surface water drainage scheme to be submitted",
        "Restricting Permitted Development Rights to manage flood risk",
    ]
    
    st.selectbox(
        label="Select the sub type of response",
        options=options,
        key="nsp_sub_type_no_objection_condition",
        on_change=update_response
    )


    selected_option = st.session_state.get("nsp_sub_type_no_objection_condition")
    if selected_option == "Secure Implementation of the FRA":
        pass
    elif selected_option == "Scheme to be agreed - Issue not addressed / addressed satisfactorily in the FRA":
        pass
    elif selected_option == "Outline Application - Scheme to be agreed at reserved matters":
        pass
    elif selected_option == "Details of an appropriate surface water drainage scheme to be submitted":
        pass
    elif selected_option == "Restricting Permitted Development Rights to manage flood risk":
        pass

def no_objection_no_condition():
    
    options = [
        "No Objections or conditions"
    ]

    st.selectbox(
        label="Select the sub type of response",
        options=options,
        key="nsp_sub_type_no_objection_no_condition",
        on_change=update_response
    )

    if st.session_state.get("nsp_sub_type_no_objection_no_condition") == "No Objections or conditions":

        st.checkbox(
            label="No Objections or conditions - No Flood Risk",
            key="nsp_no_objection_no_condition_no_flood_risk",
            on_change=update_response
        )

        st.checkbox(
            label="No Objections or conditions - Very Low Flood Risk",
            key="nsp_no_objection_no_condition_very_low_flood_risk",
            on_change=update_response
        )


def objection_in_detail():
    
    options = [
        "Exception Test Failed",
        "No FRA Submitted (where an FRA is required)",
        "No FRA Submitted (Surface Water)",
        "Inadequate FRA Submitted",
        "Risk to life or property",
        "Building Next to a Watercourse",
    ]

    st.selectbox(
        label="Select the sub type of response",
        options=options,
        key="nsp_sub_type_objection_in_detail",
        on_change=update_response
    )


    selected_option = st.session_state.get("nsp_sub_type_objection_in_detail")

    if selected_option == "Inadequate FRA Submitted":
        st.checkbox(
            label="Flood Zone has not been defined",
            key="nsp_condition_inadequate_fra_submitted_flood_zone_not_defined",
            on_change=update_response
        )
    
        st.checkbox(
            label="Development is incompatible with the Flood Zone",
            key="nsp_condition_inadequate_fra_submitted_development_incompatible_with_the_flood_zone",
            on_change=update_response
        )
        
        st.checkbox(
            label='An acceptable model has not been used - Not submitted for review',
            key="nsp_condition_inadequate_fra_submitted_acceptable_model_not_used",
            on_change=update_response
        )
        
        st.checkbox(
            label='An acceptable model has not been used - Failed to pass the review',
            key="nsp_condition_inadequate_fra_submitted_acceptable_model_not_used_failed_to_pass_the_review",
            on_change=update_response
        )

        st.checkbox(
            label='Incorrect Climate Change Allowance used',
            key="nsp_condition_inadequate_fra_submitted_incorrect_climate_change_allowance_used",
            on_change=update_response
        )

        st.checkbox(
            label='Incorrect Design Flood Level has been used (wrong node point)',
            key="nsp_condition_inadequate_fra_submitted_incorrect_design_flood_level_used_wrong_node_point",
            on_change=update_response
        )

        st.checkbox(
            label='Incorrect Design Flood Level has been used (inappropriate interpolation)',
            key="nsp_condition_inadequate_fra_submitted_incorrect_design_flood_level_used_inappropriate_interpolation",
            on_change=update_response
        )

        st.checkbox(
            label='Finished Floor Levels are not high enough',
            key="nsp_condition_inadequate_fra_submitted_finished_floor_levels_not_high_enough",
            on_change=update_response
        )

        st.checkbox(
            label='Residual Risk behind defences has not been assessed',
            key="nsp_condition_inadequate_fra_submitted_residual_risk_behind_defences_not_assessed",
            on_change=update_response
        )

        st.checkbox(
            label='Residual Risk behind defences has not been adequately assessed',
            key="nsp_condition_inadequate_fra_submitted_residual_risk_behind_defences_not_adequately_assessed",
            on_change=update_response
        )

        st.checkbox(
            label='Third Party impacts have not been assessed',
            key="nsp_condition_inadequate_fra_submitted_third_party_impacts_not_assessed",
            on_change=update_response
        )

        st.checkbox(
            label='Floodplain compensation is not Level-for-Level and Volume-for-Volume',
            key="nsp_condition_inadequate_fra_submitted_floodplain_compensation_not_level_for_level_and_volume_for_volume",
            on_change=update_response
        )
        
        st.checkbox(
            label='Floodplain compensation is not Volume-for-Volume',
            key="nsp_condition_inadequate_fra_submitted_floodplain_compensation_not_volume_for_volume",
            on_change=update_response
        )

        st.checkbox(
            label='Third Party Flood Risk mitigation measures are not adequate',
            key="nsp_condition_inadequate_fra_submitted_third_party_food_risk_mitigation_measures_not_adequate",
            on_change=update_response
        )

        st.checkbox(
            label='Access and egress routes are not properly assessed',
            key="nsp_condition_inadequate_fra_submitted_access_and_egress_routes_not_properly_assessed",
            on_change=update_response
        )

        st.checkbox(
            label='Inadequate easement from a watercourse',
            key="nsp_condition_inadequate_fra_submitted_inadequate_easement_from_a_watercourse",
            on_change=update_response
        )

        st.checkbox(
            label='Inadequate easement from a flood defence',
            key="nsp_condition_inadequate_fra_submitted_inadequate_easement_from_a_flood_defence",
            on_change=update_response
        )

        st.checkbox(
            label='Contributions not agreed',
            key="nsp_condition_inadequate_fra_submitted_contributions_not_agreed",
            on_change=update_response
        )

        st.checkbox(
            label='Flood Resilient and Resistant construction not used',
            key="nsp_condition_inadequate_fra_submitted_flood_resilient_and_resistant_construction_not_used",
            on_change=update_response
        )

        st.checkbox(
            label='Flood Resilient and Resistant construction not adequate',
            key="nsp_condition_inadequate_fra_submitted_flood_resilient_and_resistant_construction_not_adequate",
            on_change=update_response
        )



def objection_in_principle():
    
    options = [
        "Development incompatible with the Flood Zone"
    ]
    
    st.selectbox(
        label="Select the sub type of response",
        options=options,
        key="nsp_sub_type_objection_in_principle",
        on_change=update_response
    )

