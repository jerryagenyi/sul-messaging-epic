#!/usr/bin/env python3
"""
Test runner script for messaging epic Selenium tests
"""
import os
import sys
import subprocess
import argparse
from pathlib import Path

def setup_environment():
    """Setup test environment"""
    # Create necessary directories
    os.makedirs("reports", exist_ok=True)
    os.makedirs("screenshots", exist_ok=True)
    
    # Set environment variables for testing
    os.environ.setdefault('HEADLESS', 'true')
    os.environ.setdefault('TIMEOUT', '10')
    os.environ.setdefault('BASE_URL', 'https://skilledup.life')
    os.environ.setdefault('WINDOW_SIZE', '1920,1080')

def run_smoke_tests():
    """Run smoke tests only"""
    print("Running smoke tests...")
    cmd = [
        sys.executable, "-m", "pytest",
        "tests/selenium/",
        "-m", "smoke",
        "--html=reports/smoke-test-report.html",
        "--self-contained-html"
    ]
    return subprocess.run(cmd)

def run_all_tests():
    """Run all Selenium tests"""
    print("Running all Selenium tests...")
    cmd = [
        sys.executable, "-m", "pytest",
        "tests/selenium/",
        "--html=reports/full-test-report.html",
        "--self-contained-html"
    ]
    return subprocess.run(cmd)

def run_specific_test(test_name):
    """Run a specific test file or test function"""
    print(f"Running specific test: {test_name}")
    cmd = [
        sys.executable, "-m", "pytest",
        f"tests/selenium/{test_name}",
        "--html=reports/specific-test-report.html",
        "--self-contained-html"
    ]
    return subprocess.run(cmd)

def run_tests_by_marker(marker):
    """Run tests with specific marker"""
    print(f"Running tests with marker: {marker}")
    cmd = [
        sys.executable, "-m", "pytest",
        "tests/selenium/",
        "-m", marker,
        f"--html=reports/{marker}-test-report.html",
        "--self-contained-html"
    ]
    return subprocess.run(cmd)

def run_parallel_tests(workers=2):
    """Run tests in parallel using pytest-xdist"""
    print(f"Running tests in parallel with {workers} workers...")
    try:
        cmd = [
            sys.executable, "-m", "pytest",
            "tests/selenium/",
            f"-n", str(workers),
            "--html=reports/parallel-test-report.html",
            "--self-contained-html"
        ]
        return subprocess.run(cmd)
    except FileNotFoundError:
        print("pytest-xdist not installed. Install with: pip install pytest-xdist")
        return run_all_tests()

def generate_test_summary():
    """Generate test summary from reports"""
    reports_dir = Path("reports")
    if not reports_dir.exists():
        print("No reports directory found")
        return
    
    html_reports = list(reports_dir.glob("*.html"))
    xml_reports = list(reports_dir.glob("*.xml"))
    
    print("\n" + "="*50)
    print("TEST SUMMARY")
    print("="*50)
    print(f"HTML Reports: {len(html_reports)}")
    for report in html_reports:
        print(f"  - {report.name}")
    
    print(f"XML Reports: {len(xml_reports)}")
    for report in xml_reports:
        print(f"  - {report.name}")
    
    print(f"\nReports location: {reports_dir.absolute()}")

def main():
    parser = argparse.ArgumentParser(description="Run messaging epic Selenium tests")
    parser.add_argument(
        "--smoke", 
        action="store_true", 
        help="Run smoke tests only"
    )
    parser.add_argument(
        "--test", 
        type=str, 
        help="Run specific test file or function"
    )
    parser.add_argument(
        "--marker", 
        type=str, 
        help="Run tests with specific marker (smoke, integration, permissions, etc.)"
    )
    parser.add_argument(
        "--parallel", 
        type=int, 
        default=1,
        help="Run tests in parallel with specified number of workers"
    )
    parser.add_argument(
        "--headless", 
        action="store_true", 
        help="Run tests in headless mode"
    )
    parser.add_argument(
        "--base-url", 
        type=str, 
        default="https://skilledup.life",
        help="Base URL for testing"
    )
    parser.add_argument(
        "--timeout", 
        type=int, 
        default=10,
        help="Timeout for web elements (seconds)"
    )
    
    args = parser.parse_args()
    
    # Setup environment
    setup_environment()
    
    # Set environment variables from arguments
    if args.headless:
        os.environ['HEADLESS'] = 'true'
    
    os.environ['BASE_URL'] = args.base_url
    os.environ['TIMEOUT'] = str(args.timeout)
    
    # Run tests based on arguments
    result = None
    
    if args.smoke:
        result = run_smoke_tests()
    elif args.test:
        result = run_specific_test(args.test)
    elif args.marker:
        result = run_tests_by_marker(args.marker)
    elif args.parallel > 1:
        result = run_parallel_tests(args.parallel)
    else:
        result = run_all_tests()
    
    # Generate summary
    generate_test_summary()
    
    # Return exit code
    if result:
        return result.returncode
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
