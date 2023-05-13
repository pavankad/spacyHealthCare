# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pdb
from src.diag_entity_extract import medical_entity_extract
from src.icd_code_dict import icd10_dictionary


def load_diag_notes():
    #text = "CKD diabetes 3B"

    #text= "Induction of cytokine expression in leukocytes by binding of thrombin-stimulated platelets. BACKGROUND: Activated platelets tether and activate myeloid leukocytes."
    #text="Cholera due to Vibrio cholerae 01, biovar cholerae"
    """
    text="Defective survival and activation of thymocytes in transgenic mice expressing a catalytically inactive form of Ca2+/calmodulin-dependent protein kinase IV.  \
         We have generated transgenic mice that express a catalytically inactive form of Ca2+/calmodulin-dependent protein kinase IV (CaMKIV) specifically in thymic T cells\
    The presence of this protein results in a markedly reduced thymic cellularity, although the distribution of the remaining cells is normal based on evaluation of the CD4 and CD8 cell surface antigens that are used to gauge T cell development.\
    Isolated thymic T cells from the transgenic mice also show a dramatically decreased survival rate when evaluated in culture under conditions that do not favor activation.\
    When challenged with an activating stimulus such as alpha-CD3 or a combination of phorbol ester plus ionophore, the cells are severely compromised in their ability to produce the cytokine interleukin-2 (IL-2).\
    Reduction of IL-2 production is secondary to the inability to phosphorylate the cAMP response element binding protein, CREB, and induce expression of the immediate early genes such as Fos B that are required to transactivate the IL-2 promoter.\
    Because transgene expression was regulated by the proximal promoter of the murine lck gene and this promoter is inactivated in T cells that exit the thymus, the mutant hCaMKIV is not present in peripheral T cells.\
    Consequently, T lymphocytes present in the spleen can be activated normally in response to either stimulus mentioned above, demonstrating that the effects of the inactive CaMKIV on activation are reversible.\
    Our results suggest that CaMKIV may represent a physiologically relevant CREB kinase in T cells and that the enzyme is also required to ensure normal expansion of T cells in the thymus.\
    Whereas the pathway responsible for this latter role is yet to be elucidated, it is unlikely to include CREB phosphorylation."
    """
    text= "A 33-year-old white female presents after admission to the general medical/surgical hospital ward with a chief complaint \
    of shortness of breath on exertion. She reports that she was seen for similar symptoms previously at her primary care \
    physician’s office six months ago. At that time, she was diagnosed with acute bronchitis and treated with bronchodilators, \
    empiric antibiotics, and a short course oral steroid taper. This management did not improve her symptoms, and she has gradually \
    worsened over six months. She reports a 20-pound (9 kg) intentional weight loss over the past year. She denies camping, spelunking, \
    or hunting activities. She denies any sick contacts. A brief review of systems is negative for fever, night sweats, palpitations, \
    chest pain, nausea, vomiting, diarrhea, constipation, abdominal pain, neural sensation changes, muscular changes, and increased bruising\
     or bleeding. She admits a cough, shortness of breath, and shortness of breath on exertion."

    return text

def print_icd_codes(icd_codes):
    for icd_code in icd_codes:
        print("'" + icd_code[0] + "'" + " matches with Medical code: " + icd_code[2] + " with a score of: " + str(icd_code[1]))

# Press the green button in the gutter to run the script.

def main():
    #dictionary, conditions = create_icd_dict()
    pdb.set_trace()
    clinical_text = load_diag_notes()
    #instantiate model
    model = medical_entity_extract()
    #Extract diagnostic strings from clinical text
    entities = model.extract_diag_entities(clinical_text)
    #Look up ICD10 Code(Fuzzy match)
    icd10_dict = icd10_dictionary(icd10_file="icd10codes_2023.csv")
    icd_codes = icd10_dict.lkup(entities)
    print_icd_codes(icd_codes)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

if __name__=="__main__":
    main()