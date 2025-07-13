"""
Chapter 1: Logic and Proofs - Programming Applications
Discrete Mathematics for Programming

This module implements key concepts from Chapter 1, demonstrating how
propositional logic and proof techniques apply to practical programming.
"""

from typing import Dict, List, Tuple, Any, Callable
from itertools import product


class PropositionalLogic:
    """
    Implements propositional logic operations and truth table generation.
    Demonstrates Boolean algebra concepts in practical programming.
    """
    
    @staticmethod
    def logical_and(p: bool, q: bool) -> bool:
        """Basic AND operation"""
        return p and q
    
    @staticmethod
    def logical_or(p: bool, q: bool) -> bool:
        """Basic OR operation"""
        return p or q
    
    @staticmethod
    def logical_not(p: bool) -> bool:
        """Basic NOT operation"""
        return not p
    
    @staticmethod
    def logical_implies(p: bool, q: bool) -> bool:
        """
        Logical implication: p → q
        False only when p is true and q is false
        """
        return (not p) or q
    
    @staticmethod
    def logical_biconditional(p: bool, q: bool) -> bool:
        """
        Biconditional: p ↔ q
        True when p and q have the same truth value
        """
        return p == q
    
    @staticmethod
    def logical_xor(p: bool, q: bool) -> bool:
        """
        Exclusive OR: p ⊕ q
        True when exactly one of p, q is true
        """
        return p != q


class TruthTableGenerator:
    """
    Generates truth tables for logical expressions.
    Useful for exhaustive testing and logical analysis.
    """
    
    def __init__(self):
        self.operations = {
            'AND': lambda p, q: p and q,
            'OR': lambda p, q: p or q,
            'NOT': lambda p: not p,
            'IMPLIES': lambda p, q: (not p) or q,
            'BICONDITIONAL': lambda p, q: p == q,
            'XOR': lambda p, q: p != q
        }
    
    def generate_truth_table(self, variables: List[str], 
                           expression: Callable[[Dict[str, bool]], bool]) -> List[Tuple[Dict[str, bool], bool]]:
        """
        Generate a truth table for a given logical expression.
        
        Args:
            variables: List of variable names
            expression: Function that takes variable assignments and returns bool result
            
        Returns:
            List of (variable_assignment, result) tuples
        """
        truth_table = []
        
        # Generate all possible truth value assignments
        for assignment in product([False, True], repeat=len(variables)):
            var_dict = dict(zip(variables, assignment))
            result = expression(var_dict)
            truth_table.append((var_dict.copy(), result))
        
        return truth_table
    
    def print_truth_table(self, variables: List[str], 
                         expression: Callable[[Dict[str, bool]], bool],
                         expression_name: str = "Expression"):
        """Print a formatted truth table"""
        truth_table = self.generate_truth_table(variables, expression)
        
        # Print header
        header = " | ".join(variables) + f" | {expression_name}"
        print(header)
        print("-" * len(header))
        
        # Print rows
        for var_assignment, result in truth_table:
            row_values = [str(var_assignment[var])[0] for var in variables]  # T/F
            row = " | ".join(f"{val:>5}" for val in row_values)
            row += f" | {str(result)[0]:>10}"
            print(row)


class LogicalValidation:
    """
    Implements logical validation patterns commonly used in programming.
    Demonstrates practical applications of propositional logic.
    """
    
    @staticmethod
    def validate_user_input(username: str, password: str, email: str) -> Tuple[bool, List[str]]:
        """
        Validate user input using logical conditions.
        Returns (is_valid, error_messages)
        """
        errors = []
        
        # Individual validation conditions
        username_valid = len(username) >= 3 and username.isalnum()
        password_valid = len(password) >= 8 and any(c.isupper() for c in password) and any(c.isdigit() for c in password)
        email_valid = "@" in email and "." in email.split("@")[-1]
        
        if not username_valid:
            errors.append("Username must be at least 3 alphanumeric characters")
        if not password_valid:
            errors.append("Password must be at least 8 characters with uppercase and digit")
        if not email_valid:
            errors.append("Email must contain @ and valid domain")
        
        # Overall validation: all conditions must be true
        is_valid = username_valid and password_valid and email_valid
        
        return is_valid, errors
    
    @staticmethod
    def check_access_permissions(user_role: str, resource_owner: str, 
                               current_user: str, resource_public: bool) -> bool:
        """
        Check if user has access to resource using logical conditions.
        Access granted if: (admin OR owner) OR resource_public
        """
        is_admin = user_role == "admin"
        is_owner = current_user == resource_owner
        
        return (is_admin or is_owner) or resource_public


class ProofTechniques:
    """
    Demonstrates proof techniques through programming examples.
    Shows how mathematical reasoning applies to algorithm correctness.
    """
    
    @staticmethod
    def prove_array_contains_duplicate_direct(arr: List[int]) -> Tuple[bool, str]:
        """
        Direct proof approach: Check if array contains duplicates.
        If we find two identical elements, we have a duplicate.
        """
        seen = set()
        for element in arr:
            if element in seen:
                return True, f"Direct proof: Found duplicate {element}"
            seen.add(element)
        
        return False, "Direct proof: No duplicates found after checking all elements"
    
    @staticmethod
    def prove_array_contains_duplicate_contradiction(arr: List[int], max_value: int) -> Tuple[bool, str]:
        """
        Proof by contradiction: Assume no duplicates exist.
        If array length > max_possible_unique_values, contradiction!
        This demonstrates the pigeonhole principle.
        """
        if len(arr) > max_value:
            return True, (f"Proof by contradiction: Array has {len(arr)} elements "
                         f"but only {max_value} possible unique values. "
                         f"By pigeonhole principle, duplicates must exist.")
        
        # If no contradiction, check directly
        return ProofTechniques.prove_array_contains_duplicate_direct(arr)
    
    @staticmethod
    def prove_algorithm_correctness_invariant(arr: List[int]) -> Tuple[List[int], str]:
        """
        Demonstrates loop invariant proof technique.
        Proves that insertion sort maintains sorted subarray.
        """
        proof_steps = []
        result = arr.copy()
        
        proof_steps.append("Loop Invariant: Elements 0 to i-1 are sorted")
        proof_steps.append("Base case: i=1, subarray [0] is trivially sorted")
        
        for i in range(1, len(result)):
            key = result[i]
            j = i - 1
            
            # Maintain invariant: keep elements 0 to i sorted
            while j >= 0 and result[j] > key:
                result[j + 1] = result[j]
                j -= 1
            result[j + 1] = key
            
            proof_steps.append(f"Step {i}: Inserted {key}, elements 0 to {i} now sorted: {result[:i+1]}")
        
        proof_steps.append("Termination: When i = n, entire array is sorted")
        
        return result, "\n".join(proof_steps)


def demonstrate_boolean_algebra():
    """Demonstrate Boolean algebra laws with examples"""
    print("=== Boolean Algebra Demonstrations ===\n")
    
    # De Morgan's Laws
    print("De Morgan's Laws:")
    for p, q in [(True, True), (True, False), (False, True), (False, False)]:
        left = not (p and q)
        right = (not p) or (not q)
        print(f"¬(p ∧ q) ≡ ¬p ∨ ¬q: p={p}, q={q} → {left} ≡ {right} ✓" if left == right else "✗")
    
    print("\nDistributive Law:")
    for p, q, r in [(True, True, False), (False, True, True)]:
        left = p and (q or r)
        right = (p and q) or (p and r)
        print(f"p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r): p={p}, q={q}, r={r} → {left} ≡ {right}")


def demonstrate_logic_circuits():
    """Demonstrate logic circuit evaluation"""
    print("\n=== Logic Circuit Simulation ===\n")
    
    def complex_circuit(p: bool, q: bool, r: bool) -> bool:
        """
        Simulates circuit: (p ∧ ¬q) ∨ ¬r
        """
        return (p and (not q)) or (not r)
    
    print("Circuit: (p ∧ ¬q) ∨ ¬r")
    print("p | q | r | Output")
    print("--|---|---|-------")
    
    for p, q, r in product([False, True], repeat=3):
        output = complex_circuit(p, q, r)
        print(f"{int(p)} | {int(q)} | {int(r)} | {int(output)}")


if __name__ == "__main__":
    print("Chapter 1: Logic and Proofs - Programming Applications")
    print("=" * 60)
    
    # Boolean algebra demonstration
    demonstrate_boolean_algebra()
    
    # Truth table example
    print("\n=== Truth Table Generation ===")
    generator = TruthTableGenerator()
    
    # Example: (p ∧ q) → r
    def implication_example(vars_dict):
        p, q, r = vars_dict['p'], vars_dict['q'], vars_dict['r']
        return PropositionalLogic.logical_implies(p and q, r)
    
    generator.print_truth_table(['p', 'q', 'r'], implication_example, "(p ∧ q) → r")
    
    # Logic circuit demonstration
    demonstrate_logic_circuits()
    
    # Validation example
    print("\n=== Logical Validation Example ===")
    validator = LogicalValidation()
    
    test_cases = [
        ("john", "Password123", "john@email.com"),
        ("ab", "weak", "invalid-email"),
        ("admin", "StrongPass1", "admin@company.com")
    ]
    
    for username, password, email in test_cases:
        is_valid, errors = validator.validate_user_input(username, password, email)
        print(f"Input: {username}, {password}, {email}")
        print(f"Valid: {is_valid}")
        if errors:
            print(f"Errors: {errors}")
        print()
    
    # Proof technique example
    print("=== Proof Techniques Example ===")
    proof_demo = ProofTechniques()
    
    # Duplicate detection
    test_array = [1, 2, 3, 4, 2, 5]
    has_dup, proof = proof_demo.prove_array_contains_duplicate_direct(test_array)
    print(f"Array: {test_array}")
    print(f"Result: {proof}")
    
    # Proof by contradiction example
    has_dup_contradiction, proof_contradiction = proof_demo.prove_array_contains_duplicate_contradiction([1, 2, 3, 4, 5], 3)
    print(f"\nContradiction proof: {proof_contradiction}")
    
    # Loop invariant proof
    unsorted_array = [64, 34, 25, 12, 22, 11, 90]
    sorted_array, invariant_proof = proof_demo.prove_algorithm_correctness_invariant(unsorted_array)
    print(f"\n=== Loop Invariant Proof (Insertion Sort) ===")
    print(f"Original: {unsorted_array}")
    print(f"Sorted: {sorted_array}")
    print(f"\nProof steps:\n{invariant_proof}")
    
    print("\n=== Programming Applications Summary ===")
    print("✓ Boolean logic for conditional statements")
    print("✓ Truth tables for exhaustive testing")  
    print("✓ Logic circuits for hardware design")
    print("✓ Validation using logical conditions")
    print("✓ Proof techniques for algorithm correctness")
    print("✓ Mathematical reasoning in software development")
