import argparse
import math
import sys


def parse_args():
    parser = argparse.ArgumentParser(description="Credit Calculator")
    parser.add_argument("--type", type=str, help="Type of payment: annuity or diff")
    parser.add_argument("--principal", type=float, help="Loan principal")
    parser.add_argument("--periods", type=int, help="Number of months")
    parser.add_argument("--interest", type=float, help="Annual interest rate (without %)")
    parser.add_argument("--payment", type=float, help="Monthly payment")
    return parser.parse_args()


def validate(args):
    
    if args.type not in ("annuity", "diff"):
        return False

    
    if args.interest is None:
        return False

    
    if args.type == "diff" and args.payment is not None:
        return False

    
    values = [args.principal, args.periods, args.payment]
    provided = [v for v in values if v is not None]

   
    if args.type == "diff":
        if args.principal is None or args.periods is None:
            return False
    else:
        # annuity: need exactly 2 of {principal, periods, payment}
        if len(provided) != 2:
            return False

    
    all_vals = [args.interest]
    for v in [args.principal, args.periods, args.payment]:
        if v is not None:
            all_vals.append(v)
    if any(v < 0 for v in all_vals):
        return False

    return True


def monthly_rate(annual_interest):
    return annual_interest / (12 * 100)


def calc_diff(principal, periods, interest):
    i = monthly_rate(interest)
    total_paid = 0
    for m in range(1, periods + 1):
        dm = math.ceil(principal / periods + i * (principal - principal * (m - 1) / periods))
        print(f"Month {m}: payment is {dm}")
        total_paid += dm
    overpayment = total_paid - principal
    print(f"\nOverpayment = {round(overpayment)}")


def calc_annuity_payment(principal, periods, interest):
    i = monthly_rate(interest)
    a = math.ceil(principal * (i * (1 + i) ** periods) / ((1 + i) ** periods - 1))
    print(f"Your annuity payment = {a}!")
    overpayment = a * periods - principal
    print(f"Overpayment = {round(overpayment)}")


def calc_periods(principal, payment, interest):
    i = monthly_rate(interest)
    n = math.ceil(math.log(payment / (payment - i * principal), 1 + i))
    years = n // 12
    months = n % 12

    if years == 0:
        duration = f"{months} month{'s' if months != 1 else ''}"
    elif months == 0:
        duration = f"{years} year{'s' if years != 1 else ''}"
    else:
        duration = f"{years} year{'s' if years != 1 else ''} and {months} month{'s' if months != 1 else ''}"

    print(f"It will take {duration} to repay this loan!")
    overpayment = payment * n - principal
    print(f"Overpayment = {round(overpayment)}")


def calc_principal(payment, periods, interest):
    i = monthly_rate(interest)
    p = round(payment / ((i * (1 + i) ** periods) / ((1 + i) ** periods - 1)))
    print(f"Your loan principal = {p}!")
    overpayment = payment * periods - p
    print(f"Overpayment = {round(overpayment)}")


def main():
    args = parse_args()

    if not validate(args):
        print("Incorrect parameters")
        sys.exit(1)

    if args.type == "diff":
        calc_diff(args.principal, args.periods, args.interest)
    else:
        # annuity — determine which param to calculate
        if args.payment is None:
            calc_annuity_payment(args.principal, args.periods, args.interest)
        elif args.periods is None:
            calc_periods(args.principal, args.payment, args.interest)
        elif args.principal is None:
            calc_principal(args.payment, args.periods, args.interest)


if __name__ == "__main__":
    main()
