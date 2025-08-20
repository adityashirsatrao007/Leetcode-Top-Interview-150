#!/usr/bin/env python3
"""
Script to update author name in all solution files
"""

import os
import re

def update_author_in_file(file_path, new_author="Aditya Shirsatrao"):
    """Update author name in a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to match author line in different comment styles
        patterns = [
            # Python/Shell style comments
            (r'(Author:\s*)Your Name', rf'\1{new_author}'),
            # C/C++/Java style comments  
            (r'(\*\s*Author:\s*)Your Name', rf'\1{new_author}'),
        ]
        
        updated = False
        for pattern, replacement in patterns:
            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content)
                updated = True
                break
        
        if updated:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error updating {file_path}: {e}")
        return False

def main():
    base_path = "d:/Leetcode-Top-Interview-150"
    updated_count = 0
    total_files = 0
    
    # Get all problem directories
    problem_dirs = [d for d in os.listdir(base_path) 
                   if os.path.isdir(os.path.join(base_path, d)) 
                   and re.match(r'\d+-', d)]
    
    print(f"Found {len(problem_dirs)} problem directories")
    
    for problem_dir in sorted(problem_dirs):
        problem_path = os.path.join(base_path, problem_dir)
        
        # Update all solution files in this directory
        solution_files = ['solution.c', 'solution.cpp', 'Solution.java', 'solution.py']
        
        for solution_file in solution_files:
            file_path = os.path.join(problem_path, solution_file)
            if os.path.exists(file_path):
                total_files += 1
                if update_author_in_file(file_path):
                    updated_count += 1
                    print(f"Updated: {problem_dir}/{solution_file}")
    
    print(f"\nSummary:")
    print(f"Total files processed: {total_files}")
    print(f"Files updated: {updated_count}")
    print(f"Author name changed to: Aditya Shirsatrao")

if __name__ == "__main__":
    main()
