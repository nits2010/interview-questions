
## **SQL: Bond Net Present Value Calculation**

A financial firm set out to develop a query for calculating the net present value (NPV) of bond cash flows, incorporating details like annual coupons, coupons per year, face amount, and maturity date for up to three periods. The required statistic is a list of bonds and their respective NPVs.

### **Required Columns**

The result should have the following columns: `id` | `current_year` | `future_year` | `maturity_year` | `future_value` | `present_value`.

* **id**: Identifier for the bond.
* **current_year**: The present year for the calculation.
* **future_year**: Year in which the cash flow will be received.
* **maturity_year**: Maturity year of the bond.
* **future_value**: Future cash flow from the bond, rounded to two decimal places, including trailing zeros if necessary (e.g., 5.00).
* **present_value**: Discounted value of the future cash flow, using the PV equation, rounded to two decimal places, including trailing zeros if necessary (e.g., 5.00).

---

### **Constraints & Sorting**

* **Sorting**: Ascending order by `id`, then in ascending order by `future_year`.
* **Filtering**: Only bonds with a `maturity_year` greater than the current year should be included in the result.
* **Projection**: The bond cash flows should be calculated for up to **3 periods**.
* **Today's Date**: September 13, 2023.

---

### **Calculation Logic (Notes)**

**1. Future Value ($FV$)**

* `future_value = (annual_coupon / coupons_per_year) + face_amount_if_final_year`
* **annual_coupon / coupons_per_year**: Calculates the value of each individual coupon payment. For instance, if a bond pays a total annual coupon of $150.00 and it pays this coupon three times per year, then each coupon payment would be $50.00.
* **face_amount_if_final_year**: An additional amount added **only** in the year the bond matures.

**2. Present Value ($PV$)**

* `present_value = future_value / (1 + interest_rate / coupons_per_year)^(number_of_periods * coupons_per_year)`
* **interest_rate / coupons_per_year**: Adjusts the annual interest rate to the rate per coupon period. For instance, if the annual interest rate is 4% and there are 2 coupons per year, the rate per period would be 2%.
* **number_of_periods * coupons_per_year**: Adjusts the number of periods to the total number of coupon periods until the cash flow is received. For example, if a bond has 3 years to maturity and pays semi-annual coupons, there would be 6 periods in total.

---
