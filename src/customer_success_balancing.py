import argparse
import logging
import json
from typing import Optional


logging.basicConfig()
logger = logging.getLogger('customer_success_balacing')


def balance_customers(
    css: list[dict[str, int]],
    customers: list[dict[str, int]],
    absent_css: list[int] = [],
) -> int:
    """Calculate the Customer Success that servers more customers. Return 0 if there is a tie."""

    cs_more_customer_id = 0
    cs_more_customer_value = 0

    # TODO: Add params validation

    css = _remove_absent_css(css, absent_css)

    css.sort(key=lambda item: item['value'])

    for customer in customers:
        cs = _find_cs_for_customer(css, customer)

        if cs is None:
            logger.debug(f"customer {customer['id']} was not served by any cs")

        else:
            logger.debug(f"customer {customer['id']} served by cs {cs['id']}")

            cs['customer_count'] = cs.get('customer_count', 0) + 1

            if cs['customer_count'] == cs_more_customer_value:
                cs_more_customer_id = 0

            elif cs['customer_count'] > cs_more_customer_value:
                cs_more_customer_id = cs['id']
                cs_more_customer_value = cs['customer_count']

    return cs_more_customer_id


def _remove_absent_css(
    css: list[dict[str, int]],
    absent_css: list[int],
) -> list[dict[str, int]]:

    return [cs for cs in css if cs['id'] not in absent_css]


def _find_cs_for_customer(
    css: list[dict[str, int]],
    customer: dict[str, int],
) -> Optional[dict[str, int]]:

    response = None

    for cs in css:
        if cs['value'] >= customer['value']:
            response = cs

            break

    return response


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Balance customers to Customer Success")
    parser.add_argument('css', metavar="CSS", type=json.loads,
                        help="JSON containing the list of Customer Success")
    parser.add_argument('customers', metavar="CUSTOMERS", type=json.loads,
                        help="JSON containing the list of Customers")
    parser.add_argument('absent_css', metavar="ABSENT_CSS", type=json.loads,
                        help="JSON containing the list of Absent Customer Success")
    parser.add_argument('--debug', action='store_true', help="Print debug logs")
    args = parser.parse_args()

    if args.debug:
        logger.setLevel(logging.DEBUG)

    print(balance_customers(args.css, args.customers, args.absent_css))
