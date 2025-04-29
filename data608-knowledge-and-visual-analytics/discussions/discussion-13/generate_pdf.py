# %%
import os
# Import necessary WeasyPrint components
from weasyprint import HTML, CSS
# FontConfiguration is removed as its import location is causing issues
# and WeasyPrint might handle defaults automatically.

def convert_html_file_to_pdf(html_file_path, output_pdf_path):
    """
    Converts an HTML file to a PDF file using WeasyPrint, using a custom
    page size approximately 3x the height of Legal paper, and attempting
    to prevent internal page breaks in the main container.

    Args:
        html_file_path (str): The path to the input HTML file.
        output_pdf_path (str): The desired path for the output PDF file.
    """
    try:
        # Check if the input HTML file exists
        if not os.path.exists(html_file_path):
            print(f"Error: Input HTML file not found at {html_file_path}")
            return

        # Define CSS - applied in addition to any styles in the HTML file
        # Using a custom page size: Legal width (215.9mm) and 3x Legal height (1066.8mm).
        # Still attempting to avoid breaks inside the main container.
        css = CSS(string='''
            /* Specific CSS overrides or additions for PDF generation */
            @page {
                /* Custom page size: Approx. Legal width x 3 * Legal height */
                size: 215.9mm 700mm;
                margin: 1cm; /* Keep some margin */
            }
            body {
                /* Ensure fonts used in HTML are available or handled by the system */
                /* font-family is likely defined in the HTML's <style> block */
                /* Prevent potential body margin interfering with page margin */
                margin: 0;
            }
            /* Target the main content container used in the HTML */
            .max-w-4xl {
                page-break-inside: avoid !important; /* Attempt to prevent breaks within this element */
            }
        ''')

        # Create HTML object directly from the filename.
        # WeasyPrint uses the file's directory as the base_url automatically
        # for resolving relative paths (like images).
        print(f"Reading HTML from: {html_file_path}")
        html = HTML(filename=html_file_path)

        # Render the PDF
        print(f"Rendering PDF to: {output_pdf_path}")
        # Removed font_config from write_pdf call
        html.write_pdf(
            output_pdf_path,
            stylesheets=[css] # Apply our additional CSS
        )
        print("PDF generation successful!")
        print("Note: Using custom 3x Legal height page size. Check if content fits on one page.")

    except Exception as e:
        print(f"An error occurred during PDF generation: {e}")
        print("Please ensure:")
        print("1. WeasyPrint and its dependencies (Pango, Cairo, GDK-PixBuf) are installed correctly.")
        print("2. The script has permissions to write to the output path.")
        print(f"3. Image paths within the HTML file '{os.path.basename(html_file_path)}' are correct relative to its location ({os.path.dirname(html_file_path)}).")
        print("   Expected images based on previous context:")
        print("   - '01-sales-funnel.png'")
        print("   - 'data608-knowledge-and-visual-analytics/discussions/discussion-13/02-weekly-traffic.png'")
        print("   - 'data608-knowledge-and-visual-analytics/discussions/discussion-13/03-sales-distributions.png'")
        print("4. If fonts are not rendering correctly, consult the documentation for your specific WeasyPrint version regarding font configuration.")


def main():
    # --- Main part of the script ---

    # 1. Define the input HTML file path
    #    Use the absolute path provided by the user
    input_html_file = "/home/richie/work/cuny-msds/data608-knowledge-and-visual-analytics/discussions/discussion-13/output_infographic.html"

    # 2. Define the output PDF file name (will be saved in the same directory as the script)
    output_pdf = "infographic_analysis_custom_tall.pdf" # Changed output name again

    # 3. Call the conversion function
    convert_html_file_to_pdf(input_html_file, output_pdf)

# %%
main()