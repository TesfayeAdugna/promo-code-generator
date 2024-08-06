# Promo Code System

## Overview
This is a Python script to generate and manage promotional codes with a 60% discount. The generated promo codes can be used multiple times until their usage limit is reached. This system is designed to facilitate cooperation with various brands.

## Features
1. Generates unique promo codes
2. Assigns a 60% discount to promo codes
3. Tracks the usage count of each promo code
4. Validates promo codes and applies discounts
5. Returns specific messages for invalid or expired promo codes

## Prerequisites
* Python 3.11.5 or higher

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/TesfayeAdugna/promo-code-generator.git
    ```

2. Navigate to the project directory:
    ```sh
    cd promo-code-generator
    ```

## Usage

1. Run the script to generate and test promo codes:
    ```sh
    python promo_code_system.py
    ```

2. Example Output:
    ```sh
    Generated Promo code: A1B2C3D4
    Discount applied: 60%
    Discount applied: 60%
    Discount applied: 60%
    Discount applied: 60%
    Discount applied: 60%
    Expired promo code
    Expired promo code
    Expired promo code
    Expired promo code
    Expired promo code
    ```

## Approach and Challenges
Th promo code system was implemented using Python's `uuid` module to generate unique promo codes. The `PromoCodeSystem` class maintains a dictionary to store promo code details, including the discount and usage limit. The `apply_promo_code` method validates the promo code, checks its usage count, and applies the discount if the promo code is valid.

### Challenges
- Ensuring that promo codes are unique and have a consistent format.
- Handling the state of each promo code, specifically tracking the usage count and managing expired codes.
- Providing informative feedback for invalid and expired promo codes.