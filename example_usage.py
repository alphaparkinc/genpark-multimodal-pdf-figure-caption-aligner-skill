import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import MultimodalPdfFigureCaptionAlignerClient

def main():
    client = MultimodalPdfFigureCaptionAlignerClient()
    res = client.align_figures_and_captions()
    print("=== Multimodal PDF Figure Caption Aligner Output ===")
    print(f"Figures Aligned: {res['successfully_aligned_count']}/{res['total_figures_evaluated']}")
    print("\nAligned Multimodal Pairs:")
    for p in res['multimodal_units']:
        print(f"  - [{p['figure_id']} <-> {p['matched_caption_id']}] (Gap: {p['vertical_gap_px']}px):")
        print(f"    '{p['caption_text']}'")

if __name__ == '__main__':
    main()
