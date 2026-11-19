import sys

from netmiko.exceptions import NetmikoAuthenticationException, NetmikoTimeoutException

from api import ROUTER, collect_router_results


def main() -> int:
    try:
        for command, output in collect_router_results().items():
            print(f"\n--- {command} ---")
            print(output)
    except ValueError as exc:
        print(f"Configuration error: {exc}", file=sys.stderr)
        return 1
    except NetmikoAuthenticationException:
        print(
            "Router authentication failed. Check the configured credentials.",
            file=sys.stderr,
        )
        return 1
    except (NetmikoTimeoutException, OSError):
        print(
            f"Could not reach {ROUTER['ip']}:{ROUTER['port']}. "
            "Check the VM network and router address.",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
