"""Mapping of coverage gaps.

This code is automatically generated by gbd_mapping_generator/coverage_gap_builder.py

Any manual changes will be lost.
"""
from .id import reiid
from .base_template import Levels, Restrictions
from .coverage_gap_template import CoverageGap, CoverageGaps
from .cause import causes
from .risk import risk_factors


coverage_gaps = CoverageGaps(
    low_measles_vaccine_coverage_first_dose=CoverageGap(
        name='low_measles_vaccine_coverage_first_dose',
        gbd_id=reiid(318),
        distribution='dichotomous',
        restrictions=Restrictions(
            male_only=False,
            female_only=False,
            yll_only=False,
            yld_only=False,
        ),
        levels=Levels(
            cat1='exposed',
            cat2='unexposed',
        ),
        affected_causes=(causes.measles, ),
        affected_risk_factors=(),
    ),
    lack_of_immediate_assessment_and_stimulation=CoverageGap(
        name='lack_of_immediate_assessment_and_stimulation',
        gbd_id=None,
        distribution='dichotomous',
        restrictions=Restrictions(
            female_only=False,
            male_only=False,
            yld_only=False,
            yll_only=False,
        ),
        levels=Levels(
            cat1='exposed',
            cat2='unexposed',
        ),
        affected_causes=(causes.neonatal_preterm_birth_complications, ),
        affected_risk_factors=(),
    ),
    lack_of_hiv_positive_antiretroviral_treatment=CoverageGap(
        name='lack_of_hiv_positive_antiretroviral_treatment',
        gbd_id=None,
        distribution='dichotomous',
        restrictions=Restrictions(
            male_only=False,
            female_only=False,
            yll_only=False,
            yld_only=False,
        ),
        levels=Levels(
            cat1='exposed',
            cat2='unexposed',
        ),
        affected_causes=(causes.hiv_aids_resulting_in_other_diseases, ),
        affected_risk_factors=(),
    ),
    lack_of_lipid_lowering_therapy=CoverageGap(
        name='lack_of_lipid_lowering_therapy',
        gbd_id=None,
        distribution='polytomous',
        restrictions=Restrictions(
            female_only=False,
            male_only=False,
            yld_only=False,
            yll_only=False,
        ),
        levels=Levels(
            cat1='NONE',
            cat10='FLUVASTATIN_80',
            cat11='SIMVASTATIN_10',
            cat12='PRAVASTATIN_40',
            cat13='LOVASTATIN_40',
            cat14='PRAVASTATIN_80',
            cat15='SIMVASTATIN_20',
            cat16='LOVASTATIN_60',
            cat17='ATORVASTATIN_10',
            cat18='FLUVASTATIN_20+EZETIMIBE',
            cat19='PRAVASTATIN_10+EZETIMIBE',
            cat2='OTHER',
            cat20='ROSUVASTATIN_5',
            cat21='SIMVASTATIN_40',
            cat22='LOVASTATIN_10+EZETIMIBE',
            cat23='SIMVASTATIN_5+EZETIMIBE',
            cat24='FLUVASTATIN_40+EZETIMIBE',
            cat25='LOVASTATIN_20+EZETIMIBE',
            cat26='PRAVASTATIN_20+EZETIMIBE',
            cat27='ATORVASTATIN_20',
            cat28='FLUVASTATIN_80+EZETIMIBE',
            cat29='SIMVASTATIN_10+EZETIMIBE',
            cat3='FLUVASTATIN_20',
            cat30='ROSUVASTATIN_10',
            cat31='SIMVASTATIN_80',
            cat32='LOVASTATIN_40+EZETIMIBE',
            cat33='PRAVASTATIN_40+EZETIMIBE',
            cat34='ATORVASTATIN_40',
            cat35='PRAVASTATIN_80+EZETIMIBE',
            cat36='SIMVASTATIN_20+EZETIMIBE',
            cat37='LOVASTATIN_60+EZETIMIBE',
            cat38='ROSUVASTATIN_20',
            cat39='ATORVASTATIN_10+EZETIMIBE',
            cat4='PRAVASTATIN_10',
            cat40='ATORVASTATIN_80',
            cat41='ROSUVASTATIN_5+EZETIMIBE',
            cat42='SIMVASTATIN_40+EZETIMIBE',
            cat43='ROSUVASTATIN_40',
            cat44='ATORVASTATIN_20+EZETIMIBE',
            cat45='ROSUVASTATIN_10+EZETIMIBE',
            cat46='SIMVASTATIN_80+EZETIMIBE',
            cat47='ATORVASTATIN_40+EZETIMIBE',
            cat48='ROSUVASTATIN_20+EZETIMIBE',
            cat49='ATORVASTATIN_80+EZETIMIBE',
            cat5='LOVASTATIN_10',
            cat50='ROSUVASTATIN_40+EZETIMIBE',
            cat6='SIMVASTATIN_5',
            cat7='FLUVASTATIN_40',
            cat8='LOVASTATIN_20',
            cat9='PRAVASTATIN_20',
        ),
        affected_causes=(),
        affected_risk_factors=(),
    ),
    lack_of_breastfeeding_promotion=CoverageGap(
        name='lack_of_breastfeeding_promotion',
        gbd_id=None,
        distribution='dichotomous',
        restrictions=Restrictions(
            female_only=False,
            male_only=False,
            yld_only=False,
            yll_only=False,
        ),
        levels=Levels(
            cat1='exposed',
            cat2='unexposed',
        ),
        affected_causes=(),
        affected_risk_factors=(risk_factors.discontinued_breastfeeding, ),
    ),
    low_oral_rehydration_solution_coverage=CoverageGap(
        name='low_oral_rehydration_solution_coverage',
        gbd_id=None,
        distribution='dichotomous',
        restrictions=Restrictions(
            male_only=False,
            female_only=False,
            yll_only=False,
            yld_only=False,
        ),
        levels=Levels(
            cat1='exposed',
            cat2='unexposed',
        ),
        affected_causes=(causes.diarrheal_diseases, ),
        affected_risk_factors=(),
    ),
)
