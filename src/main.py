import sys
import logging
from core.scanner import Scanner
from core.analyzer import Analyzer
from config import Config

def main():
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    
    # Load configuration
    config = Config()
    logging.info("Configuration loaded.")

    # Initialize scanner and analyzer
    scanner = Scanner(config)
    analyzer = Analyzer()

    # Perform network scan
    logging.info("Starting network scan...")
    scan_results = scanner.scan_network()
    
    # Analyze scan results
    logging.info("Analyzing scan results...")
    analysis_results = analyzer.analyze_results(scan_results)

    # Generate report
    logging.info("Generating report...")
    analyzer.generate_report(analysis_results)

    logging.info("Process completed successfully.")

if __name__ == "__main__":
    main()