import streamlit as st
from generate_response.generate_response import update_response

def render_overview():
    """Render the content for the Overview tab"""

    st.subheader("FRA and Relevant Documents")

    # Has the FRA been submitted?
    fra_submitted = st.toggle(
        "Has the FRA been submitted?",
        key="fra_submitted",
        on_change=update_response
    )

    if fra_submitted:
        # Get FRA details (e.g. 'FRA TITLE', revision 1, dated 1 January 2025)
        fra_details = st.text_input(
            label="Enter the FRA details",
            key="fra_details",
            on_change=update_response,
            help="Enter the FRA details as a string, e.g. 'FRA TITLE', revision 1, dated 1 January 2025"
        )
    
    # Have other relevant documents been submitted?
    relevant_documents_submitted = st.toggle(
        "Have other relevant documents been submitted?",
        key="relevant_documents_submitted",
        on_change=update_response
    )

    # If relevant documents have been submitted, ask for the documents
    if relevant_documents_submitted:
        relevant_documents = st.text_input(
            label="Enter the relevant documents",
            key="relevant_documents",
            on_change=update_response,
            help="Enter the relevant documents as a string, e.g. 'FRA TITLE', revision 1, dated 1 January 2025"
        )
    

    # Add a divider and subheader
    st.divider()
    st.subheader("Devlopment Details")

    # Get the application type
    # Select box - Full, Outline, Reserved Matters, Hybrid, Change of Use
    application_type = st.selectbox(
        "What type of application is this?",
        ["Full", "Outline", "Reserved Matters", "Hybrid", "Change of Use"],
        key="application_type",
        on_change=update_response,
        index=0
    )

    if application_type == "Change of Use":

        # ask for the existing vulerablity classification
        existing_vulnerability_classification = st.selectbox(
            "What is the existing vulerability classification?",
            ['Water Compatible', 'Less Vulnerable', 'More Vulnerable', 'Highly Vulnerable', 'Essential Infrastructure'],
            key="existing_vulnerability_classification",
            on_change=update_response,
            index=0
        )

    # Ask for the proposed vulerability classification
    proposed_vulnerability_classification = st.selectbox(
        "What is the proposed vulerability classification?",
        ['Water Compatible', 'Less Vulnerable', 'More Vulnerable', 'Highly Vulnerable', 'Essential Infrastructure'],
        key="proposed_vulnerability_classification",
        on_change=update_response,
        index=0
    )


    # Add a divider and subheader
    st.divider()
    st.subheader("Flood Zone and Modelling")

    # Has the flood zone been defined?
    flood_zone_defined = st.toggle(
        "Has the flood zone been defined?",
        key="flood_zone_defined",
        on_change=update_response
    )
    
    # If the flood zone has been defined, ask for the flood zone
    if flood_zone_defined:
        # Flood Zone - multiple choice
        flood_zone = st.multiselect(
            "Flood Zone",
            ["Flood zone 1", "Flood zone 2", "Flood zone 3a", "Flood zone 3b"],
            key="flood_zone",
            on_change=update_response,
            placeholder='Select all that apply'
        )
    
        # Only show flood zone model if "Not defined" is not selected
        if flood_zone != "Not defined":
            # Flood zones based on - radio buttons
            flood_model = st.radio(
                "Flood zones based on",
                ["EA Model", "New National Modelling", "Applicant Model"],
                key="flood_model",
                on_change=update_response
            )
            
            # Model status - only show if not "Not defined" and not "New National Modelling"
            if flood_model != "New National Modelling":
                model_status = st.radio(
                    "Model status",
                    ["Not Reviewed (review not needed)", "Not Reviewed (review needed)", "Reviewed and approved", "Reviewed and rejected", 'Approved EA Model', 'EA Model not suitable to be used for this site'],
                    key="model_status",
                    on_change=update_response
                )
            
            # if the model used is an EA ask for the name and year
            if flood_model == "EA Model":
                model_name = st.text_input(
                    "Model name",
                    key="model_name",
                    on_change=update_response
                )

                model_year = st.number_input(
                    "Model year",
                    key="model_year",
                    on_change=update_response,
                    min_value=1900,
                    max_value=2100,
                    value=2020,
                    step=1
                )

    

    # Add a divider and subheader
    st.divider()
    st.subheader("Climate Change")

    # ask if climate change is relevant
    climate_change_relevant = st.toggle(
        "Is climate change relevant to this application?",
        key="climate_change_relevant",
        on_change=update_response
    )

    if not climate_change_relevant:
        # ask for the reason
        climate_change_reason = st.text_area(
            "Why is climate change not relevant to this application?",
            key="climate_change_reason",
            on_change=update_response
        )
    else:
        # What climate change allowance has been used (number input between 0 and 200)
        climate_change_allowance = st.number_input(
            label="What climate change allowance has been used?",
            min_value=0,
            max_value=200,
            value=0,
            on_change=update_response,
            help="Enter the climate change allowance as a percentage",
            key="climate_change_allowance"
        )

        # is this the correct climate change allowance (checkbox)
        correct_climate_change_allowance = st.toggle(
            "Is this the correct climate change allowance?",
            key="correct_climate_change_allowance",
            on_change=update_response
        )

        # if its not the correct climate change allowance, ask for the correct one
        if not correct_climate_change_allowance:
            correct_climate_change_allowance_value = st.number_input(
                "What is the correct climate change allowance?",
                min_value=0,
                max_value=200,
                value=0,
                on_change=update_response,
                key="correct_climate_change_allowance_value"
            )



    # Add a divider and subheader
    st.divider()
    st.subheader("Finished Floor Levels")

    # ask if finished floor levels are relevant
    finished_floor_levels_relevant = st.toggle(
        "Are finished floor levels relevant to this application?",
        key="finished_floor_levels_relevant",
        on_change=update_response
    )



    if finished_floor_levels_relevant:

        # ask if they have been provided
        finished_floor_levels_provided = st.toggle(
            "Have finished floor levels been provided?",
            key="finished_floor_levels_provided",
            on_change=update_response
        )

        if finished_floor_levels_provided:
            # ask for the finished floor levels
            finished_floor_levels = st.number_input(
                "What are the finished floor levels?",
                key="finished_floor_levels",
                on_change=update_response
            )

            # ask if the finished floor levels are acceptable
            finished_floor_levels_acceptable = st.toggle(
                "Are the finished floor levels acceptable?",
                key="finished_floor_levels_acceptable",
                on_change=update_response
            )

            # if the finished floor levels are not acceptable, ask for the reason
            if not finished_floor_levels_acceptable:
                finished_floor_levels_reason = st.radio(
                    label="Why are the finished floor levels not acceptable?",
                    options=['insufficient information provided', 'insufficient freeboard', 'the Design Flood Level is unknown', 'Other'],
                    key="finished_floor_levels_reason",
                    on_change=update_response
                )

                # if other, ask for the reason
                if finished_floor_levels_reason == "Other":
                    finished_floor_levels_reason_other = st.text_input(
                        "Why are the finished floor levels not acceptable?",
                        key="finished_floor_levels_reason_other",
                        on_change=update_response
                    )

    
    




    # Add a divider and subheader
    st.divider()
    st.subheader("Flood Defences")

    # Are there any flood relevant flood defences?
    flood_defences = st.toggle(
        "Are there any flood relevant flood defences?",
        key="flood_defences",
        on_change=update_response
    )

    # If there are flood relevant flood defences, ask how many there are
    if flood_defences:

        flood_defences_count = st.number_input(
            "How many flood relevant flood defences are there?",
            key="flood_defences_count",
            on_change=update_response,
            min_value=1,
            max_value=100,
            value=1,
            help="Don't think of assets think functional defences. e.g. a wall part of scheme a made of of 5 assets would be 1 defence"
        )

        # Create inputs for each flood defence
        for i in range(int(flood_defences_count)):
            st.write(f"**Flood Defence {i+1}**")
            
            # Input for defence name
            st.text_input(
                "Defence Name",
                key=f"defence_name_{i}",
                on_change=update_response
            )
            
            # Input for Standard of Protection (SOP)
            st.number_input(
                "Standard of Protection (SOP)",
                key=f"defence_sop_{i}",
                on_change=update_response,
                min_value=1,
                max_value=1000,
                value=100,
                help="Enter the Standard of Protection (return period) for this defence"
            )
            
            st.divider()
        

        # Is breach and over topping analysis needed?
        breach_and_over_topping_analysis = st.toggle(
            "Is breach and over topping analysis needed?",
            key="breach_and_over_topping_analysis",
            on_change=update_response
        )

        if breach_and_over_topping_analysis:

            # ask has it been done?
            breach_and_over_topping_analysis_done = st.toggle(
                "Has it been done?",
                key="breach_and_over_topping_analysis_done",
                on_change=update_response
            )

            # if it has been done, is it acceptable?
            if breach_and_over_topping_analysis_done:
                acceptable_breach_and_over_topping_analysis = st.toggle(
                    "Is it acceptable?",
                    key="acceptable_breach_and_over_topping_analysis",
                    on_change=update_response
                )
            
                # if it is not acceptable, ask for the reason
                if not acceptable_breach_and_over_topping_analysis:
                    breach_and_over_topping_analysis_reason = st.text_input(
                        "Why is it not acceptable?",
                        key="breach_and_over_topping_analysis_reason",
                        on_change=update_response
                    )
                
                # If it is acceptable what does it show (checkbox - at risk or not at risk)
                if acceptable_breach_and_over_topping_analysis:
                    breach_and_over_topping_analysis_result = st.toggle(
                        "Is the site at risk still in a breach and overtopping scenario?",
                        key="breach_and_over_topping_analysis_result",
                        on_change=update_response
                    )
    

    # add a divider and subheader
    st.divider()
    st.subheader("Third Party Impacts")

    # Does the devlopment displace flood water in the design flood event
    # radio buttons - yes or no, unknown
    development_displaces_flood_water = st.radio(
        "Does the devlopment displace flood water in the design flood event?",
        ["Yes", "No", "Unknown"],
        key="development_displaces_flood_water",
        on_change=update_response
    )

    # if yes, ask if mitigation has been put in place
    if development_displaces_flood_water == "Yes":
        mitigation_put_in_place = st.toggle(
            "Has mitigation been put in place?",
            key="mitigation_put_in_place",
            on_change=update_response
        )

        if mitigation_put_in_place:

            # if mitigation has been put in place it flood plain compensation or other mitigation
            # radio buttons - flood plain compensation or other mitigation
            mitigation_type = st.radio(
                "What type of mitigation has been put in place?",
                ["Flood plain compensation", "Other mitigation"],
                key="mitigation_type",
                on_change=update_response
            )

            # if flood plain compensation, ask for type
            # radio buttons - L4L & V4V - V4V - Not L4L & V4V
            if mitigation_type == "Flood plain compensation":
                flood_plain_compensation_type = st.radio(
                    "What is the flood plain compensation?",
                    ["Level-for-Level and Volume-for-Volume", "Volume-for-Volume", "Not Level-for-Level and Volume-for-Volume"],
                    key="flood_plain_compensation_type",
                    on_change=update_response
                )
            
            # if other mitigation, ask for the type
            if mitigation_type == "Other mitigation":
                mitigation_other_type = st.text_input(
                    "What is the other mitigation?",
                    key="mitigation_other_type",
                    on_change=update_response
                )
            
            # ask if mitigation is acceptable
            mitigation_acceptable = st.toggle(
                "Is the mitigation acceptable?",
                key="mitigation_acceptable",
                on_change=update_response
            )

            # if mitigation is not acceptable, ask for the reason
            if not mitigation_acceptable:
                mitigation_acceptable_reason = st.text_area(
                    "Why is the mitigation acceptable or not acceptable?",
                    key="mitigation_acceptable_reason",
                    on_change=update_response
                )
    
    # add a divider and subheader
    st.divider()
    st.subheader("Design Flood Level")

    # ask if the design flood level has been calculated
    design_flood_level_calculated = st.toggle(
        "Has the design flood level been included in the FRA?",
        key="design_flood_level_calculated",
        on_change=update_response
    )

    if design_flood_level_calculated:
        design_flood_level = st.number_input(
            "What is the design flood level?",
            key="design_flood_level",
            on_change=update_response
        )

        # ask if the design flood level is acceptable
        design_flood_level_acceptable = st.toggle(
            "Is the design flood level acceptable?",
            key="design_flood_level_acceptable",
            on_change=update_response
        )

        if not design_flood_level_acceptable:

            # ask for the reason
            # radio buttons - model has not been accepted, incorrect climate change, incorrect node point used
            design_flood_level_reason = st.radio(
                "Why is the design flood level not acceptable?",
                ["the model has not been accepted", "it uses an incorrect climate change allowance", "it uses an incorrect node point", "Other"],
                key="design_flood_level_reason",
                on_change=update_response
            )

            # if other, ask for the reason
            if design_flood_level_reason == "Other":
                design_flood_level_reason_other = st.text_area(
                    "Why is the design flood level not acceptable?",
                    key="design_flood_level_reason_other",
                    on_change=update_response
                )
    


    # add a divider and subheader
    st.divider()
    st.subheader("Access and Egress")

    # ask if access and egress has been considered
    access_and_egress_considered = st.toggle(
        "Has access and egress been considered?",
        key="access_and_egress_considered",
        on_change=update_response
    )

    if access_and_egress_considered:
        # what is the access and egress position
        # radio buttons - Dry, Very Low,Danger to Some, Danger to Most, Danger to All
        access_and_egress_position = st.radio(
            "What does the FRA state the access and egress position is?",
            ["Dry", "Very Low", "Danger to Some", "Danger to Most", "Danger to All", "Other"],
            key="access_and_egress_position",
            on_change=update_response
        )

        # if other, ask for the position
        if access_and_egress_position == "Other":
            access_and_egress_position_other = st.text_input(
                "What is the access and egress position?",
                key="access_and_egress_position_other",
                on_change=update_response
            )

        # ask if we agree with the position
        access_and_egress_position_agreed = st.radio(
            "Do we agree with the position?",
            ["Yes", "No", "Not enough information provided"],
            key="access_and_egress_position_agreed",
            on_change=update_response
        )



    # Ask if we are providing data on the risk as part of this response
    access_and_egress_data = st.toggle(
        "Are we providing data on the risk as part of this response?",
        key="access_and_egress_data",
        on_change=update_response
    )

    # if we are providing data on the risk, ask for the data
    if access_and_egress_data:
        access_and_egress_data_text = st.text_area(
            "What does the data we have say about the access and egress risk?",
            key="access_and_egress_data_text",
            on_change=update_response
        )
        




    # add a divider and subheader
    st.divider()
    st.subheader("Easement")

    # ask if there is an issue with the easement
    # radio buttons - yes or no, unclear
    easement_issue = st.radio(
        "Is there an issue with the easement?",
        ["Yes", "No", "Unclear"],
        key="easement_issue",
        on_change=update_response
    )

    # ask for the reason
    easement_issue_reason = st.text_area(
        "Why is this our position on the easement?",
        key="easement_issue_reason",
        on_change=update_response
    )

    # if there is an issue with the easement or its unclear, ask what the resolution is
    if easement_issue == "Yes" or easement_issue == "Unclear":
        easement_resolution = st.text_area(
            "What is the resolution to the easement issue?",
            key="easement_resolution",
            on_change=update_response
        )


    # add a divider and subheader
    st.divider()
    st.subheader("Required Contributions")

    # ask if there will be any required contributions
    # radio buttons - yes or no
    required_contributions = st.radio(
        "Will there be any required contributions?",
        ["Yes", "No"],
        key="required_contributions",
        on_change=update_response
    )

    if required_contributions == "Yes":

        # ask what the contributions are for
        # multiselect - maintenance of a flood defences assets, flood warning service, maintenance of watercourse, other
        required_contributions_type = st.multiselect(
            "What are the contributions?",
            ["Maintenance of a flood defences assets", "Flood warning service", "Maintenance of watercourse", "Other"],
            key="required_contributions_type",
            on_change=update_response
        )

        # if other is one of the contributions, ask for the other contribution
        if "Other" in required_contributions_type:
            required_contributions_other = st.text_area(
                "What is the other contribution?",
                key="required_contributions_other",
                on_change=update_response
            )
        

        # ask for the total contributions required
        total_contributions_required = st.number_input(
            label="What is the total contributions required? (in £)",
            key="total_contributions_required",
            step=1,
            on_change=update_response
        )

        # ask for why they are required
        required_contributions_reason = st.text_area(
            "Why are contributions required?",
            key="required_contributions_reason",
            on_change=update_response
        )
    

    # Add a divider and subheader
    st.divider()
    st.subheader("Flood Reslient and Resistant Construction")   

    # ask if the development is using flood resilient and resistant construction
    # radio buttons - yes or no
    flood_resilient_and_resistant_construction = st.radio(
        "Is the development using flood resilient and resistant construction?",
        ["Yes", "No"],
        key="flood_resilient_and_resistant_construction",
        on_change=update_response
    )

    # if yes, ask if it is acceptable
    if flood_resilient_and_resistant_construction == "Yes":
        flood_resilient_and_resistant_construction_acceptable = st.toggle(
            "Is the development flood resilient and resistant construction acceptable?",
            key="flood_resilient_and_resistant_construction_acceptable",
            on_change=update_response
        )

        # if it is not acceptable, ask for the reason
        if not flood_resilient_and_resistant_construction_acceptable:
            flood_resilient_and_resistant_construction_reason = st.text_area(
                "Why is the development flood resilient and resistant construction not acceptable?",
                key="flood_resilient_and_resistant_construction_reason",
                on_change=update_response
            )
    
    if flood_resilient_and_resistant_construction == "No":
        # ask if this is acceptable 
        flood_resilient_and_resistant_construction_acceptable = st.toggle(
            "Is the development not using flood resilient and resistant construction acceptable?",
            key="flood_resilient_and_resistant_construction_acceptable",
            on_change=update_response
        )

        # ask for the reason
        flood_resilient_and_resistant_construction_reason = st.text_area(
            "Why is this acceptable?",
            key="flood_resilient_and_resistant_construction_reason",
            on_change=update_response
        )


    # Add a divider and subheader
    st.divider()
    st.subheader("Other Information")
    
    # Original overview text area
    st.text_area(label="Add any additional information here", 
                value="", 
                height=200,
                key="overview_input",
                on_change=update_response)