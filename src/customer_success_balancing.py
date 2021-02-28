import argparse
import logging
import json


logging.basicConfig()
logger = logging.getLogger('customer_success_balacing')


def balance_customers(
    css: list[dict[str, int]], customers: list[dict[str, int]], absent_css: list[int] = [],
) -> int:
    """Calculate the Customer Success that servers more customers. Return 0 if there is a tie."""

    cs_more_customer_id = 0
    cs_more_customer_value = 0

    # TODO: Add params validation

    css = [cs for cs in css if cs['id'] not in absent_css]

    css.sort(key=lambda item: item['value'])

    for customer in customers:
        for cs in css:
            if cs['value'] >= customer['value']:
                logger.debug(f"customer {customer['id']} served by cs {cs['id']}")

                cs['customer_count'] = cs.get('customer_count', 0) + 1

                if cs['customer_count'] == cs_more_customer_value:
                    cs_more_customer_id = 0

                elif cs['customer_count'] > cs_more_customer_value:
                    cs_more_customer_id = cs['id']
                    cs_more_customer_value = cs['customer_count']

                break

        else:
            logger.debug(f"customer {customer['id']} was not served by any cs")

    return cs_more_customer_id


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Balance customers to Customer Success")
    parser.add_argument('css', metavar="CSS", type=json.loads,
                        help="JSON containing the list of Customer Success")
    parser.add_argument('customers', metavar="CUSTOMERS", type=json.loads,
                        help="JSON containing the list of Customers")
    parser.add_argument('absent_css', metavar="ABSENT_CSS", type=json.loads,
                        help="JSON containing the list of Absent Customer Success")
    parser.add_argument('--debug', action='store_true', help="Prints debug logs")
    args = parser.parse_args()

    if args.debug:
        logger.setLevel(logging.DEBUG)

    print(balance_customers(args.css, args.customers, args.absent_css))
